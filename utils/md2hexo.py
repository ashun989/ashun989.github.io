# import re
# import os

# PICT_RE = "!\[.*\]\(.*\)"

# def chg_pict(old_path, new_path):
#     rule = re.compile(PICT_RE)
#     with open(old_path, "r") as rfp:
#         with open(new_path, "w") as wfp:
#             while True:
#                 line = rfp.readline()
#                 if not line:
#                     break
#                 ans = rule.match(line)
#                 sub_line = line[ans.start():ans.end()]
#                 l1 = sub_line.split('(')
#                 pict_name = l1[1].split(')')[0]
#                 pict_name = pict_name.split('/')[-1]
#                 print(pict_name)
#                 wline = "{ asset_img"
#                 wfp.write()

# if __name__ == "__main__":

