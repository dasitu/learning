import requests
import json
import datetime
import threading
import getpass


class GerritHelper:
    def __init__(self, host="https://gerrite1.ext.net.nokia.com/"):
        user = input("gerrit username:")
        password = getpass.getpass(prompt=f"gerrit password for {user}:")
        self.host = host
        self.auth = (user, password)
        if not self.validate_user():
            exit("invalid username or password")

    def validate_user(self):
        url = f'{self.host}/a/accounts/self/detail'
        response = requests.get(url, auth=self.auth)
        if response.status_code == 200:
            return True
        return False

    def get_change_details(self, change_id):
        url = f'{self.host}/changes/{change_id}/detail?pp=0'
        print(f'{self.host}/#/c/{change_id}')
        # gerrit special output format
        # To prevent against Cross Site Script Inclusion (XSSI) attacks,
        # the JSON response body starts with a magic prefix line
        # that must be stripped before feeding the rest of the response body to a JSON parser
        valid_json = requests.get(url).text[5:]
        change_details = json.loads(valid_json)
        return change_details

    def set_review_comments(self, change_id, patch_set, json_comments):
        if not self.validate_user():
            print("user validate failed for :", self.auth[0])
            return False

        response = requests.post(f'{self.host}/a/changes/{change_id}/revisions/{patch_set}/review', json=json_comments, auth=self.auth)
        if response.status_code == "200":
            return True
        return False

    def auto_rft(self, change_ids, checking_interval=3600.0):
        # auth represent (user, password)
        # check_interval in seconds
        if len(change_ids) == 0:
            exit("watched changes list is empty")

        t = threading.Timer(checking_interval, self.auto_rft, [change_ids, checking_interval])
        t.start()
        current_time = datetime.datetime.now()
        print(f"---------------{current_time}---------------")

        merged_count = 0
        for change_id in change_ids:
            change_details = self.get_change_details(change_id)

            status = change_details["status"]
            if status == "MERGED":
                merged_count += 1
                print("change is merged")
                continue

            messages = change_details["messages"]
            last_message = messages[-1]['message']
            patch_set = messages[-1]["_revision_number"]
            print(f'last message of patch set[{patch_set}]:')
            print(last_message)

            if "FAILURE" in last_message:
                self.set_review_comments(change_id, patch_set, "rft")
            else:
                print("last message does not contain FAILURE, do nothing")
            print("=======================================")

        if merged_count == len(change_ids):
            t.cancel()
            print("all watched changes are merged.")
            exit(0)
        print("--------------------------------------------------------\n")


if __name__ == '__main__':
    watched_changes = [1031855, 1031894, 1026665]
    gerrit_helper = GerritHelper()
    gerrit_helper.auto_rft(watched_changes)
