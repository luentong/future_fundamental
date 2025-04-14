import akshare as ak
import pandas as pd
#
# for sym in ["¶¹Ò»","¶¹¶þ","»¦ÂÁ","»¦Í­","Ïð½º","¶¹ÆÉ","ÃÞ»¨","È¼ÓÍ","ÓñÃ×","¶¹ÓÍ","PTA","»¦Ð¿","ËÜÁÏ","×Øéµ","»Æ½ð","ÂÝÎÆ¸Ö","PVC",
#             "»¦Ç¦","½¹Ì¿","°×Òø","²ËÓÍ","²£Á§","²ËÆÉ","½¹Ãº","Á¤Çà","Ìú¿óÊ¯","¼¦µ°","PP","ÈÈÔþ¾í°å","ÃÌ¹è","¹èÌú","ÓñÃ×µí·Û","»¦Îý",
#             "»¦Äø","Ô­ÓÍ","ÃÞÉ´","Ö½½¬","ÒÒ¶þ´¼","ºìÔæ","ÄòËØ","20ºÅ½º","²»Ðâ¸Ö","±½ÒÒÏ©","´¿¼î","°×ÌÇ"]:
#
#     test = ["Æ»¹û","¼×´¼","ÖÐÖ¤500","ÉÏÖ¤50","5ÄêÆÚ¹úÕ®"]
#     futures_zh_realtime_df = None
#     try:
#         futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
#     except:
#         print(sym + " ´íÎó")
#         continue
#     # print(type(futures_zh_realtime_df))
#     # print(futures_zh_realtime_df)
#     # with pd.option_context('display.max_rows', None,
#     #                        'display.max_columns', None,
#     #                        'display.precision', 3,
#     #                        ):
#     #     print(futures_zh_realtime_df)
#
#     rows = len(futures_zh_realtime_df.axes[0])
#     cols = len(futures_zh_realtime_df.axes[1])
#     df = futures_zh_realtime_df.iloc[1:rows]
#
#
#     df = df.sort_values("name").reset_index()
#
#     diffs = []
#     names = []
#     prev = ""
#     for i in range(0,rows-1):
#         if i == 0:
#             names.append(df.loc[i, "trade"])
#         #print(df.iloc[[i]])
#         # print(df.loc[i, "name"])
#         # print(df.loc[i, "trade"])
#         if not prev:
#             prev = float(df.loc[i, "trade"])
#         else:
#             diffs.append(prev - float(df.loc[i, "trade"]))
#             prev = float(df.loc[i, "trade"])
#         names.append(df.loc[i, "name"])
#         if i == rows-2:
#             names.append(df.loc[i, "trade"])
#
#     print(diffs)
#     print(names)
#     print('\n')

################################################½¹Ãº½¹Ì¿################################################################

futures_zh_realtime_df = None
sym = "½¹Ãº"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
names_jiaomei = []
prices = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaomei.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices)
print('\n')

futures_zh_realtime_df = None
sym = "½¹Ì¿"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
prices_jiaotan = []
names_jiaotan = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_jiaotan.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaotan.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices_jiaotan)
print('\n')

final = []
final_names = []
if len(names_jiaomei) >= len(names_jiaotan):
    j = 0
    k = 0
    for i in range(len(names_jiaotan)):
        if j >= len(names_jiaomei) or k >= len(names_jiaotan):
            break
        break_all = False
        while names_jiaomei[j][-4:] != names_jiaotan[k][-4:]:
            if float(names_jiaomei[j][-4:]) < float(names_jiaotan[k][-4:]):
                j += 1
            else:
                k += 1
            if j >= len(names_jiaomei) or k >= len(names_jiaotan):
                break_all = True
                break
        if break_all:
            break
        final_names.append(names_jiaomei[k][-4:])
        final.append(prices_jiaotan[k] - 1.33*prices[j])
        j += 1
        k += 1


print(final_names)
print(final)
print('\n')

################################################¶¹ÆÉ²ËÆÉ################################################################

futures_zh_realtime_df = None
sym = "¶¹ÆÉ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
names_jiaomei = []
prices = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaomei.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices)
print('\n')

futures_zh_realtime_df = None
sym = "²ËÆÉ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
prices_jiaotan = []
names_jiaotan = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_jiaotan.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaotan.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices_jiaotan)
print('\n')

final = []
final_names = []
if len(names_jiaomei) >= len(names_jiaotan):
    j = 0
    for i in range(len(names_jiaotan)):
        while names_jiaomei[j][-4:] != names_jiaotan[i][-4:]:
            j += 1
        final_names.append(names_jiaomei[j][-4:])
        final.append( prices[j] / prices_jiaotan[i])
        j += 1


print(final_names)
print(final)
print('\n')


################################################PTA¶ÌÏË################################################################

futures_zh_realtime_df = None
sym = "PTA"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
names_jiaomei = []
prices = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaomei.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices)
print('\n')

futures_zh_realtime_df = None
sym = "¶ÌÏË"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
prices_jiaotan = []
names_jiaotan = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_jiaotan.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaotan.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices_jiaotan)
print('\n')

final = []
final_names = []
if len(names_jiaomei) >= len(names_jiaotan):
    j = 0
    k = 0
    for i in range(len(names_jiaotan)):
        if j >= len(names_jiaomei) or k >= len(names_jiaotan):
            break
        break_all = False
        while names_jiaomei[j][-4:] != names_jiaotan[k][-4:]:
            if float(names_jiaomei[j][-4:]) < float(names_jiaotan[k][-4:]):
                j += 1
            else:
                k += 1
            if j >= len(names_jiaomei) or k >= len(names_jiaotan):
                break_all = True
                break
        if break_all:
            break
        final_names.append(names_jiaomei[k][-4:])
        final.append(prices_jiaotan[k] - 1.33*prices[j])
        j += 1
        k += 1



print(final_names)
print(final)
print('\n')

################################################ÂÝÎÆÈÈ¾í################################################################

futures_zh_realtime_df = None
sym = "È¼ÓÍ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
names_jiaomei = []
prices = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaomei.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices)
print('\n')

futures_zh_realtime_df = None
sym = "µÍÁòÈ¼ÁÏÓÍ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
prices_jiaotan = []
names_jiaotan = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_jiaotan.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaotan.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices_jiaotan)
print('\n')

final = []
final_names = []
if len(names_jiaomei) >= len(names_jiaotan):
    j = 0
    k = 0
    for i in range(len(names_jiaotan)):
        if j >= len(names_jiaomei) or k >= len(names_jiaotan):
            break
        break_all = False
        while names_jiaomei[j][-4:] != names_jiaotan[k][-4:]:
            if float(names_jiaomei[j][-4:]) < float(names_jiaotan[k][-4:]):
                j += 1
            else:
                k += 1
            if j >= len(names_jiaomei) or k >= len(names_jiaotan):
                break_all = True
                break
        if break_all:
            break
        final_names.append(names_jiaomei[k][-4:])
        final.append(prices_jiaotan[k] - 1.33*prices[j])
        j += 1
        k += 1


print(final_names)
print(final)
print('\n')

################################################PTA¶ÌÏË################################################################

futures_zh_realtime_df = None
sym = "ÂÝÎÆ¸Ö"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
names_jiaomei = []
prices = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaomei.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices)
print('\n')

futures_zh_realtime_df = None
sym = "ÈÈÔþ¾í°å"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
prices_jiaotan = []
names_jiaotan = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_jiaotan.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaotan.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices_jiaotan)
print('\n')

final = []
final_names = []
if len(names_jiaomei) >= len(names_jiaotan):
    j = 0
    for i in range(len(names_jiaotan)):
        while names_jiaomei[j][-4:] != names_jiaotan[i][-4:]:
            j += 1
        final_names.append(names_jiaomei[j][-4:])
        final.append( - prices[j] + prices_jiaotan[i])
        j += 1


print(final_names)
print(final)
print('\n')

################################################Á¤ÇàÈ¼ÓÍ################################################################

futures_zh_realtime_df = None
sym = "Á¤Çà"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
names_jiaomei = []
prices = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaomei.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices)
print('\n')

futures_zh_realtime_df = None
sym = "È¼ÓÍ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
prices_jiaotan = []
names_jiaotan = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_jiaotan.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaotan.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices_jiaotan)
print('\n')

final = []
final_names = []
if len(names_jiaomei) >= len(names_jiaotan):
    j = 0
    k = 0
    for i in range(len(names_jiaotan)):
        if j >= len(names_jiaomei) or k >= len(names_jiaotan):
            break
        break_all = False
        while names_jiaomei[j][-4:] != names_jiaotan[k][-4:]:
            if float(names_jiaomei[j][-4:]) < float(names_jiaotan[k][-4:]):
                j += 1
            else:
                k += 1
            if j >= len(names_jiaomei) or k >= len(names_jiaotan):
                break_all = True
                break
        if break_all:
            break
        final_names.append(names_jiaomei[k][-4:])
        final.append(prices_jiaotan[k] - 1.33*prices[j])
        j += 1
        k += 1


print(final_names)
print(final)
print('\n')


################################################Á¤ÇàÈ¼ÓÍ################################################################

futures_zh_realtime_df = None
sym = "¶¹¶þ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
names_jiaomei = []
prices = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaomei.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices)
print('\n')

futures_zh_realtime_df = None
sym = "¶¹Ò»"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
prices_jiaotan = []
names_jiaotan = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_jiaotan.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaotan.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices_jiaotan)
print('\n')

final = []
final_names = []
if len(names_jiaomei) >= len(names_jiaotan):
    j = 0
    for i in range(len(names_jiaotan)):
        while names_jiaomei[j][-4:] != names_jiaotan[i][-4:]:
            j += 1
        final_names.append(names_jiaomei[j][-4:])
        final.append(prices[j] - prices_jiaotan[i])
        j += 1


print(final_names)
print(final)
print('\n')

################################################¶¹ÓÍ²ËÓÍ################################################################

futures_zh_realtime_df = None
sym = "¶¹ÓÍ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
names_jiaomei = []
prices = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaomei.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices)
print('\n')

futures_zh_realtime_df = None
sym = "²ËÓÍ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
prices_jiaotan = []
names_jiaotan = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_jiaotan.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaotan.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices_jiaotan)
print('\n')

final = []
final_names = []
if len(names_jiaomei) >= len(names_jiaotan):
    j = 0
    for i in range(len(names_jiaotan)):
        while names_jiaomei[j][-4:] != names_jiaotan[i][-4:]:
            j += 1
        final_names.append(names_jiaomei[j][-4:])
        final.append(-prices[j] + prices_jiaotan[i])
        j += 1


print(final_names)
print(final)
print('\n')


################################################¶¹ÓÍ¶¹ÆÉ################################################################

futures_zh_realtime_df = None
sym = "¶¹ÓÍ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
names_jiaomei = []
prices = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaomei.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices)
print('\n')

futures_zh_realtime_df = None
sym = "¶¹ÆÉ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
prices_jiaotan = []
names_jiaotan = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_jiaotan.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaotan.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices_jiaotan)
print('\n')

final = []
final_names = []
if len(names_jiaomei) >= len(names_jiaotan):
    j = 0
    for i in range(len(names_jiaotan)):
        while names_jiaomei[j][-4:] != names_jiaotan[i][-4:]:
            j += 1
        final_names.append(names_jiaomei[j][-4:])
        final.append(prices[j] / prices_jiaotan[i])
        j += 1


print(final_names)
print(final)
print('\n')


################################################¶¹ÓÍ×ØéµÓÍ################################################################

futures_zh_realtime_df = None
sym = "×Øéµ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
names_jiaomei = []
prices = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaomei.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices)
print('\n')

futures_zh_realtime_df = None
sym = "¶¹ÓÍ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
prices_jiaotan = []
names_jiaotan = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_jiaotan.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaotan.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices_jiaotan)
print('\n')

final = []
final_names = []
if len(names_jiaomei) >= len(names_jiaotan):
    j = 0
    for i in range(len(names_jiaotan)):
        while names_jiaomei[j][-4:] != names_jiaotan[i][-4:]:
            j += 1
        final_names.append(names_jiaomei[j][-4:])
        final.append(-prices[j] + prices_jiaotan[i])
        j += 1


print(final_names)
print(final)
print('\n')

################################################²ËÓÍ×ØéµÓÍ################################################################

futures_zh_realtime_df = None
sym = "×Øéµ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
names_jiaomei = []
prices = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaomei.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices)
print('\n')

futures_zh_realtime_df = None
sym = "²ËÓÍ"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
prices_jiaotan = []
names_jiaotan = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_jiaotan.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaotan.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names)
print(prices_jiaotan)
print('\n')

final = []
final_names = []
if len(names_jiaomei) >= len(names_jiaotan):
    j = 0
    for i in range(len(names_jiaotan)):
        while names_jiaomei[j][-4:] != names_jiaotan[i][-4:]:
            j += 1
        final_names.append(names_jiaomei[j][-4:])
        final.append(-prices[j] + prices_jiaotan[i])
        j += 1


print(final_names)
print(final)
print('\n')

################################################¸Ö³§ÀûÈó################################################################

futures_zh_realtime_df = None
sym = "ÂÝÎÆ¸Ö"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
names_luowen = []
prices_luowen = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_luowen.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_luowen.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names_luowen)
print(prices_luowen)
print('\n')

futures_zh_realtime_df = None
sym = "Ìú¿óÊ¯"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
prices_tiekuang = []
names_tiekuang = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_tiekuang.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_tiekuang.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names_tiekuang)
print(prices_tiekuang)
print('\n')



futures_zh_realtime_df = None
sym = "½¹Ì¿"
try:
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
except:
    print(sym + " ´íÎó")
# print(type(futures_zh_realtime_df))
# print(futures_zh_realtime_df)
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_realtime_df)

rows = len(futures_zh_realtime_df.axes[0])
cols = len(futures_zh_realtime_df.axes[1])
df = futures_zh_realtime_df.iloc[1:rows]


df = df.sort_values("name").reset_index()

diffs = []
names = []
prices_jiaotan = []
names_jiaotan = []
prev = ""
for i in range(0,rows-2):
    if i == 0:
        names.append(df.loc[i, "trade"])
    #print(df.iloc[[i]])
    # print(df.loc[i, "name"])
    # print(df.loc[i, "trade"])
    prices_jiaotan.append(float(df.loc[i, "trade"]))
    if not prev:
        prev = float(df.loc[i, "trade"])
    else:
        diffs.append(prev - float(df.loc[i, "trade"]))
        prev = float(df.loc[i, "trade"])
    names.append(df.loc[i, "name"])
    names_jiaotan.append(df.loc[i, "name"])
    if i == rows-3:
        names.append(df.loc[i, "trade"])

print(diffs)
print(names_jiaotan)
print(prices_jiaotan)
print('\n')



final = []
final_names = []
if len(names_jiaotan) <= len(names_tiekuang):
    j = 0
    k = 0
    for i in range(len(names_jiaotan)):
        while names_tiekuang[j][-4:] != names_jiaotan[i][-4:]:
            j += 1
            k += 1
        while names_tiekuang[j][-4:] != names_luowen[k][-4:]:
            k += 1
        final_names.append(names_jiaotan[i][-4:])
        final.append(prices_luowen[k] - 2.4*prices_tiekuang[j] - 0.68*prices_jiaotan[i] - 250)
        j += 1
        k += 1

print("¸Ö³§ÀûÈó")
print(final_names)
print(final)
print('\n')