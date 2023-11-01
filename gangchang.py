import akshare as ak
import pandas as pd

# futures_zh_realtime_df = None
# sym = "Ìú¿ó"
# try:
#     futures_zh_realtime_df = ak.futures_zh_realtime(symbol=sym)
# except:
#     print(sym + " ´íÎó")
# # print(type(futures_zh_realtime_df))
# # print(futures_zh_realtime_df)
# # with pd.option_context('display.max_rows', None,
# #                        'display.max_columns', None,
# #                        'display.precision', 3,
# #                        ):
# #     print(futures_zh_realtime_df)
#
# rows = len(futures_zh_realtime_df.axes[0])
# cols = len(futures_zh_realtime_df.axes[1])
# df = futures_zh_realtime_df.iloc[1:rows]
#
#
# df = df.sort_values("name").reset_index()

import akshare as ak

for sym in ["1701","1705","1710","1801","1805","1810","1901","1905","1910","2001","2005","2010",
            "2101","2105","2110","2201","2205","2210","2301","2305","2310","2401","2405","2410"]:
    try:
        futures_zh_daily_sina_df = ak.futures_zh_daily_sina(symbol="i" + sym)
        with pd.option_context('display.max_rows', None,
                               'display.max_columns', None,
                               'display.precision', 3,
                               ):
            #print(futures_zh_daily_sina_df)
            i_data = futures_zh_daily_sina_df[['date','open']]

        futures_zh_daily_sina_df = ak.futures_zh_daily_sina(symbol="rb"  + sym)
        with pd.option_context('display.max_rows', None,
                               'display.max_columns', None,
                               'display.precision', 3,
                               ):
            #print(futures_zh_daily_sina_df)
            rb_data = futures_zh_daily_sina_df[['date', 'open']]

        futures_zh_daily_sina_df = ak.futures_zh_daily_sina(symbol="j"  + sym)
        with pd.option_context('display.max_rows', None,
                               'display.max_columns', None,
                               'display.precision', 3,
                               ):
            #print(futures_zh_daily_sina_df)
            j_data = futures_zh_daily_sina_df[['date', 'open']]

        futures_zh_daily_sina_df = ak.futures_zh_daily_sina(symbol="jm"  + sym)
        with pd.option_context('display.max_rows', None,
                               'display.max_columns', None,
                               'display.precision', 3,
                               ):
            #print(futures_zh_daily_sina_df)
            jm_data = futures_zh_daily_sina_df[['date', 'open']]
    except Exception as e:
        print(e)
        print(sym + " continue")
        continue
    rb_datas = []
    i_datas = []
    j_datas = []
    jm_datas = []

    for i in range(len(rb_data)):
        # print(rb_data.loc[i,"date"])
        # print(rb_data.loc[i, "open"])
        rb_datas.append([rb_data.loc[i,"date"],rb_data.loc[i, "open"]])

    for i in range(len(i_data)):
        # print(i_data.loc[i,"date"])
        # print(i_data.loc[i, "open"])
        i_datas.append([i_data.loc[i,"date"], i_data.loc[i, "open"]])

    for i in range(len(j_data)):
        # print(j_data.loc[i,"date"])
        # print(j_data.loc[i, "open"])
        j_datas.append([j_data.loc[i,"date"], j_data.loc[i, "open"]])

    for i in range(len(jm_data)):
        # print(jm_data.loc[i,"date"])
        # print(jm_data.loc[i, "open"])
        jm_datas.append([jm_data.loc[i,"date"], jm_data.loc[i, "open"]])

    final = []
    for rb in rb_datas:
        i_index = -1
        j_index = -1
        jm_index = -1
        i_ind = 0
        for i in i_datas:
            if i[0] == rb[0]:
                i_index = i_ind
                break
            i_ind += 1
        jm_ind = 0
        for jm in jm_datas:
            if jm[0] == rb[0]:
                jm_index = jm_ind
                break
            jm_ind += 1
        j_ind = 0
        for j in j_datas:
            if j[0] == rb[0]:
                j_index = j_ind
                break
            j_ind += 1

        if i_index != -1 and j_index != -1:
            final.append([rb[1] - 2.4 * i_datas[i_index][1] - 0.68 * j_datas[j_index][1] - 250, rb[0]])
            # print(rb[0])
        elif i_index != -1 and jm_index != -1:
            final.append([rb[1] - 2.4 * i_datas[i_index][1] - 0.68 * (jm_datas[jm_index][1] * 1.33 + 80) - 250, rb[0]])
            # print(rb[0], "jm")


    print(final, "final" + sym)
    print("___________________________________")


######################################################¶¹ÓÍ¶¹ÆÉ¼Û²î#############################################

for sym in ["1701","1705","1710","1801","1805","1810","1901","1905","1910","2001","2005","2010",
            "2101","2105","2110","2201","2205","2210","2301","2305","2310","2401","2405","2410"]:
    try:


        futures_zh_daily_sina_df = ak.futures_zh_daily_sina(symbol="m" + sym)
        with pd.option_context('display.max_rows', None,
                               'display.max_columns', None,
                               'display.precision', 3,
                               ):
            print(futures_zh_daily_sina_df)
            j_data = futures_zh_daily_sina_df[['date', 'open']]

        futures_zh_daily_sina_df = ak.futures_zh_daily_sina(symbol="y" + sym)
        with pd.option_context('display.max_rows', None,
                               'display.max_columns', None,
                               'display.precision', 3,
                               ):
            print(futures_zh_daily_sina_df)
            jm_data = futures_zh_daily_sina_df[['date', 'open']]
    except:
        print("´íÎó" + sym)
        continue

    j_datas = []
    jm_datas = []


    for i in range(len(j_data)):
        print(j_data.loc[i,"date"])
        print(j_data.loc[i, "open"])
        j_datas.append([j_data.loc[i,"date"], j_data.loc[i, "open"]])

    for i in range(len(jm_data)):
        print(jm_data.loc[i,"date"])
        print(jm_data.loc[i, "open"])
        jm_datas.append([jm_data.loc[i,"date"], jm_data.loc[i, "open"]])

    final = []
    for j in j_datas:

        jm_index = -1

        jm_ind = 0
        for jm in jm_datas:
            if jm[0] == j[0]:
                jm_index = jm_ind
                break
            jm_ind += 1


        if jm_index != -1:
            final.append([jm_datas[jm_index][1] / j[1] , j[0]])
            print(j[0])
            print(j[1])
            print(jm[1])


    print(final, "final")


# #####################################################½¹Ãº½¹Ì¿¼Û²î############################################
#
#
# import akshare as ak
#
#
# futures_zh_daily_sina_df = ak.futures_zh_daily_sina(symbol="j2210")
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_daily_sina_df)
#     j_data = futures_zh_daily_sina_df[['date', 'open']]
#
# futures_zh_daily_sina_df = ak.futures_zh_daily_sina(symbol="jm2210")
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_daily_sina_df)
#     jm_data = futures_zh_daily_sina_df[['date', 'open']]
#
#
# j_datas = []
# jm_datas = []
#
#
# for i in range(len(j_data)):
#     print(j_data.loc[i,"date"])
#     print(j_data.loc[i, "open"])
#     j_datas.append([j_data.loc[i,"date"], j_data.loc[i, "open"]])
#
# for i in range(len(jm_data)):
#     print(jm_data.loc[i,"date"])
#     print(jm_data.loc[i, "open"])
#     jm_datas.append([jm_data.loc[i,"date"], jm_data.loc[i, "open"]])
#
# final = []
# for j in j_datas:
#
#     jm_index = -1
#
#     jm_ind = 0
#     for jm in jm_datas:
#         if jm[0] == j[0]:
#             jm_index = jm_ind
#             break
#         jm_ind += 1
#
#
#     if jm_index != -1:
#         final.append([j[1] - 1.33 * jm_datas[jm_index][1], j[0]])
#         print(j[0])
#         print(j[1])
#         print(jm[1])
#
#
# print(final, "final")

#
# #####################################################¶¹ÆÉ²ËÆÉ¼Û²î############################################
#
#
# import akshare as ak
#
#
# futures_zh_daily_sina_df = ak.futures_zh_daily_sina(symbol="rm2401")
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_daily_sina_df)
#     j_data = futures_zh_daily_sina_df[['date', 'open']]
#
# futures_zh_daily_sina_df = ak.futures_zh_daily_sina(symbol="m2401")
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(futures_zh_daily_sina_df)
#     jm_data = futures_zh_daily_sina_df[['date', 'open']]
#
#
# j_datas = []
# jm_datas = []
#
#
# for i in range(len(j_data)):
#     print(j_data.loc[i,"date"])
#     print(j_data.loc[i, "open"])
#     j_datas.append([j_data.loc[i,"date"], j_data.loc[i, "open"]])
#
# for i in range(len(jm_data)):
#     print(jm_data.loc[i,"date"])
#     print(jm_data.loc[i, "open"])
#     jm_datas.append([jm_data.loc[i,"date"], jm_data.loc[i, "open"]])
#
# final = []
# for j in j_datas:
#
#     jm_index = -1
#
#     jm_ind = 0
#     for jm in jm_datas:
#         if jm[0] == j[0]:
#             jm_index = jm_ind
#             break
#         jm_ind += 1
#
#
#     if jm_index != -1:
#         final.append([jm_datas[jm_index][1] / j[1] , j[0]])
#         print(j[0])
#         print(j[1])
#         print(jm[1])
#
#
# print(final, "final")
