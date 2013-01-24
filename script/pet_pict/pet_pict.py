#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib import script

ID = (
	90000584, #桃ハート
	90000586, #緑ハート
	90000585, #藍ハート
	90000587, #山吹ハート
	90000588, #菫ハート
	90000589, #茜ハート
	90000590, #杏ハート
	90000591, #空ハート
	90000592, #胡桃ハート
	90000593, #若菜ハート
	90000594, #白ハート
	90000595, #黒ハート
	90000424, #ネコマタ（桃）用おでかけパーカー
	90000542, #ネコマタ（桃）用メイド服
	90000367, #ネコマタ（桃）キティラー服
	90000390, #ネコマタ（緑）用カントリー服
	90000482, #ネコマタ（緑）用戦闘制服
	90000362, #ネコマタ（藍）用羽衣
	90000443, #ネコマタ（藍）用黒セーラー
	90000528, #ネコマタ（藍）用リボンワンピース
	90000403, #ネコマタ（山吹）用和装
	90000524, #ネコマタ（山吹）用ボーイッシュ服
	90000418, #ネコマタ（菫）用おめかしワンピ
	90000499, #ネコマタ（菫）用着物ワンピ
	90000404, #ネコマタ（茜）用ハロウィン服
	90000436, #ネコマタ（茜）用チャイナドレス
	90000339, #ネコマタ（杏）用セーラー
	90000448, #ネコマタ（杏）用エルブンジャケット
	90000410, #ネコマタ（空）用怪盗服
	90000475, #ネコマタ（空）用さざなみのワンピース
	90000432, #ネコマタ（胡桃・若菜）用メイド服
	90000357, #ネコマタ（胡桃・若菜）用水着
	90000511, #ネコマタ(胡桃・若菜)用カボチャマント
	90000391, #ネコマタ（白）用トップモデル服
	90000449, #ネコマタ（白）用ウェディングドレス
	90000513, #ネコマタ（白）用カボチャマント
	90000343, #ネコマタ（黒）用騎士服
	90000425, #ネコマタ（黒）用巫女服
	90000512, #ネコマタ（黒）用カボチャマント
	90000514, #ネコマタ（ミケ）用カボチャマント
	90000515, #ネコマタ（トラ）用カボチャマント
	90000516, #ネコマタ（アリス）用カボチャマント
	90000517, #アメジスト用カボチャマント
	90000518, #ルビー用カボチャマント
	90000519, #トパーズ用カボチャマント
	90000520, #サファイア用カボチャマント
	90000521, #ダイヤモンド用カボチャマント
	90000668, #シモツキ用フェイブルハート（白）
)

ITEM_EVENT_ID = {
	#item_id: (pet_id, pet_pict_id)
	20050198: (10260000, 10260087), #ネコマタハート（桃）
	20050199: (10260050, 10260088), #ネコマタハート（緑）
	20050200: (10260051, 10260089), #ネコマタハート（藍）
	20050201: (10260052, 10260090), #ネコマタハート（山吹）
	20050202: (10260003, 10260091), #ネコマタハート（菫）
	20050203: (10260004, 10260092), #ネコマタハート（茜）
	20050204: (10260005, 10260093), #ネコマタハート（杏）
	20050205: (10260006, 10260094), #ネコマタハート（空）
	20050206: (14240000, 10260095), #ネコマタハート（胡桃）
	20050207: (14240000, 10260096), #ネコマタハート（若菜）
	20050208: (14380000, 10260097), #ネコマタハート（白）
	20050209: (14370000, 10260098), #ネコマタハート（黒）
	#チェックリボンハート
	20050210: (10260000, 10260099), #桃用チェックリボンハート
	20050211: (10260051, 10260100), #藍用チェックリボンハート
	20050212: (10260050, 10260101), #緑用チェックリボンハート
	20050213: (10260052, 10260102), #山吹用チェックリボンハート
	20050214: (10260003, 10260103), #菫用チェックリボンハート
	20050215: (10260004, 10260104), #茜用チェックリボンハート
	20050216: (10260005, 10260105), #杏用チェックリボンハート
	20050217: (10260006, 10260106), #空用チェックリボンハート
	20050218: (14240000, 10260107), #胡桃用チェックリボンハート
	20050219: (14240000, 10260108), #若菜用チェックリボンハート
	20050220: (14380000, 10260109), #白用チェックリボンハート
	20050221: (14370000, 10260110), #黒用チェックリボンハート
	#シャーマンハート
	20050222: (10260000, 10260111), #桃用シャーマンハート
	20050223: (10260051, 10260112), #藍用シャーマンハート
	20050224: (10260050, 10260113), #緑用シャーマンハート
	20050225: (10260052, 10260114), #山吹用シャーマンハート
	20050226: (10260003, 10260115), #菫用シャーマンハート
	20050227: (10260004, 10260116), #茜用シャーマンハート
	20050228: (10260005, 10260117), #杏用シャーマンハート
	20050229: (10260006, 10260118), #空用シャーマンハート
	20050230: (14240000, 10260119), #胡桃用シャーマンハート
	20050231: (14240000, 10260120), #若菜用シャーマンハート
	20050232: (14380000, 10260121), #白用シャーマンハート
	20050233: (14370000, 10260122), #黒用シャーマンハート
	#ファーコーデハート
	20050235: (10260000, 10260123), #桃用ファーコーデハート
	20050236: (10260051, 10260124), #藍用ファーコーデハート
	20050237: (10260050, 10260125), #緑用ファーコーデハート
	20050238: (10260052, 10260126), #山吹用ファーコーデハート
	20050239: (10260003, 10260127), #菫用ファーコーデハート
	20050240: (10260004, 10260128), #茜用ファーコーデハート
	20050241: (10260005, 10260129), #杏用ファーコーデハート
	20050242: (10260006, 10260130), #空用ファーコーデハート
	20050243: (14240000, 10260131), #胡桃用ファーコーデハート
	20050244: (14240000, 10260132), #若菜用ファーコーデハート
	20050245: (14380000, 10260133), #白用ファーコーデハート
	20050246: (14370000, 10260134), #黒用ファーコーデハート
	#盗賊ハート
	20050248: (10260000, 10260135), #桃用盗賊ハート
	20050249: (10260051, 10260136), #藍用盗賊ハート
	20050250: (10260050, 10260137), #緑用盗賊ハート
	20050251: (10260052, 10260138), #山吹用盗賊ハート
	20050252: (10260003, 10260139), #菫用盗賊ハート
	20050253: (10260004, 10260140), #茜用盗賊ハート
	20050254: (10260005, 10260141), #杏用盗賊ハート
	20050255: (10260006, 10260142), #空用盗賊ハート
	20050256: (14240000, 10260143), #胡桃用盗賊ハート
	20050257: (14240000, 10260144), #若菜用盗賊ハート
	20050258: (14380000, 10260145), #白用盗賊ハート
	20050259: (14370000, 10260146), #黒用盗賊ハート
	#キンダーハート
	20050261: (10260000, 10260147), #桃用キンダーハート
	20050262: (10260051, 10260148), #藍用キンダーハート
	20050263: (10260050, 10260149), #緑用キンダーハート
	20050264: (10260052, 10260150), #山吹用キンダーハート
	20050265: (10260003, 10260151), #菫用キンダーハート
	20050266: (10260004, 10260152), #茜用キンダーハート
	20050267: (10260005, 10260153), #杏用キンダーハート
	20050268: (10260006, 10260154), #空用キンダーハート
	20050269: (14240000, 10260155), #胡桃用キンダーハート
	20050270: (14240000, 10260156), #若菜用キンダーハート
	20050271: (14380000, 10260157), #白用キンダーハート
	20050272: (14370000, 10260158), #黒用キンダーハート
	#カンフーハート
	20050274: (10260000, 10260159), #桃用カンフーハート
	20050275: (10260051, 10260160), #藍用カンフーハート
	20050276: (10260050, 10260161), #緑用カンフーハート
	20050277: (10260052, 10260162), #山吹用カンフーハート
	20050278: (10260003, 10260163), #菫用カンフーハート
	20050279: (10260004, 10260164), #茜用カンフーハート
	20050280: (10260005, 10260165), #杏用カンフーハート
	20050281: (10260006, 10260166), #空用カンフーハート
	20050282: (14240000, 10260167), #胡桃用カンフーハート
	20050283: (14240000, 10260168), #若菜用カンフーハート
	20050284: (14380000, 10260169), #白用カンフーハート
	20050285: (14370000, 10260170), #黒用カンフーハート
	#桃用みやびハート
	20050288: (10260000, 10260171), #桃用みやびハート
	20050289: (10260051, 10260172), #藍用みやびハート
	20050290: (10260050, 10260173), #緑用みやびハート
	20050291: (10260052, 10260174), #山吹用みやびハート
	20050292: (10260003, 10260175), #菫用みやびハート
	20050293: (10260004, 10260176), #茜用みやびハート
	20050294: (10260005, 10260177), #杏用みやびハート
	20050295: (10260006, 10260178), #空用みやびハート
	20050296: (14240000, 10260179), #胡桃用みやびハート
	20050297: (14240000, 10260180), #若菜用みやびハート
	20050298: (14380000, 10260181), #白用みやびハート
	20050299: (14370000, 10260182), #黒用みやびハート
	#チルドレンハート
	20050301: (10260000, 10260183), #桃用チルドレンハート
	20050302: (10260051, 10260184), #藍用チルドレンハート
	20050303: (10260050, 10260185), #緑用チルドレンハート
	20050304: (10260052, 10260186), #山吹用チルドレンハート
	20050305: (10260003, 10260187), #菫用チルドレンハート
	20050306: (10260004, 10260188), #茜用チルドレンハート
	20050307: (10260005, 10260189), #杏用チルドレンハート
	20050308: (10260006, 10260190), #空用チルドレンハート
	20050309: (14240000, 10260191), #胡桃用チルドレンハート
	20050310: (14240000, 10260192), #若菜用チルドレンハート
	20050311: (14380000, 10260193), #白用チルドレンハート
	20050312: (14370000, 10260194), #黒用チルドレンハート
	#やんちゃハート
	20050314: (10260000, 10260195), #桃用やんちゃハート
	20050315: (10260051, 10260196), #藍用やんちゃハート
	20050316: (10260050, 10260197), #緑用やんちゃハート
	20050317: (10260052, 10260198), #山吹用やんちゃハート
	20050318: (10260003, 10260199), #菫用やんちゃハート
	20050319: (10260004, 10260200), #茜用やんちゃハート
	20050320: (10260005, 10260201), #杏用やんちゃハート
	20050321: (10260006, 10260202), #空用やんちゃハート
	20050322: (14240000, 10260203), #胡桃用やんちゃハート
	20050323: (14240000, 10260204), #若菜用やんちゃハート
	20050324: (14380000, 10260205), #白用やんちゃハート
	20050325: (14370000, 10260206), #黒用やんちゃハート
	#フェアリーハート
	20050327: (10260000, 10260207), #桃用フェアリーハート
	20050328: (10260051, 10260208), #藍用フェアリーハート
	20050329: (10260050, 10260209), #緑用フェアリーハート
	20050330: (10260052, 10260210), #山吹用フェアリーハート
	20050331: (10260003, 10260211), #菫用フェアリーハート
	20050332: (10260004, 10260212), #茜用フェアリーハート
	20050333: (10260005, 10260213), #杏用フェアリーハート
	20050334: (10260006, 10260214), #空用フェアリーハート
	20050335: (14240000, 10260215), #胡桃用フェアリーハート
	20050336: (14240000, 10260216), #若菜用フェアリーハート
	20050337: (14380000, 10260217), #白用フェアリーハート
	20050338: (14370000, 10260218), #黒用フェアリーハート
	#エキゾチックハート
	20050340: (10260000, 10260219), #桃用エキゾチックハート
	20050341: (10260051, 10260220), #藍用エキゾチックハート
	20050342: (10260050, 10260221), #緑用エキゾチックハート
	20050343: (10260052, 10260222), #山吹用エキゾチックハート
	20050344: (10260003, 10260223), #菫用エキゾチックハート
	20050345: (10260004, 10260224), #茜用エキゾチックハート
	20050346: (10260005, 10260225), #杏用エキゾチックハート
	20050347: (10260006, 10260226), #空用エキゾチックハート
	20050348: (14240000, 10260227), #胡桃用エキゾチックハート
	20050349: (14240000, 10260228), #若菜用エキゾチックハート
	20050350: (14380000, 10260229), #白用エキゾチックハート
	20050351: (14370000, 10260230), #黒用エキゾチックハート
	#エレガントハート
	20050353: (10260000, 10260231), #桃用エレガントハート
	20050354: (10260051, 10260232), #藍用エレガントハート
	20050355: (10260050, 10260233), #緑用エレガントハート
	20050356: (10260052, 10260234), #山吹用エレガントハート
	20050357: (10260003, 10260235), #菫用エレガントハート
	20050358: (10260004, 10260236), #茜用エレガントハート
	20050359: (10260005, 10260237), #杏用エレガントハート
	20050360: (10260006, 10260238), #空用エレガントハート
	20050361: (14240000, 10260239), #胡桃用エレガントハート
	20050362: (14240000, 10260240), #若菜用エレガントハート
	20050363: (14380000, 10260241), #白用エレガントハート
	20050364: (14370000, 10260242), #黒用エレガントハート
	#アイシクルハート
	20050367: (10260000, 10260243), #桃用アイシクルハート
	20050368: (10260050, 10260244), #緑用アイシクルハート
	20050369: (10260051, 10260245), #藍用アイシクルハート
	20050370: (10260052, 10260246), #山吹用アイシクルハート
	20050371: (10260003, 10260247), #菫用アイシクルハート
	20050372: (10260004, 10260248), #茜用アイシクルハート
	20050373: (10260005, 10260249), #杏用アイシクルハート
	20050374: (10260006, 10260250), #空用アイシクルハート
	20050375: (14240000, 10260251), #胡桃用アイシクルハート
	20050376: (14240000, 10260252), #若菜用アイシクルハート
	20050377: (14380000, 10260253), #白用アイシクルハート
	20050378: (14370000, 10260254), #黒用アイシクルハート
	#マリンハート
	20050380: (10260000, 10260255), #桃用マリンハート
	20050381: (10260050, 10260256), #緑用マリンハート
	20050382: (10260051, 10260257), #藍用マリンハート
	20050383: (10260052, 10260258), #山吹用マリンハート
	20050384: (10260003, 10260259), #菫用マリンハート
	20050385: (10260004, 10260260), #茜用マリンハート
	20050386: (10260005, 10260261), #杏用マリンハート
	20050387: (10260006, 10260262), #空用マリンハート
	20050388: (14240000, 10260263), #胡桃用マリンハート
	20050389: (14240000, 10260264), #若菜用マリンハート
	20050390: (14380000, 10260265), #白用マリンハート
	20050391: (14370000, 10260266), #黒用マリンハート
	#アラビアンハート
	20050393: (10260000, 10260267), #桃用アラビアンハート
	20050394: (10260051, 10260268), #藍用アラビアンハート
	20050395: (10260050, 10260269), #緑用アラビアンハート
	20050396: (10260052, 10260270), #山吹用アラビアンハート
	20050397: (10260003, 10260271), #菫用アラビアンハート
	20050398: (10260004, 10260272), #茜用アラビアンハート
	20050399: (10260005, 10260273), #杏用アラビアンハート
	20050400: (10260006, 10260274), #空用アラビアンハート
	20050401: (14240000, 10260275), #胡桃用アラビアンハート
	20050402: (14240000, 10260276), #若菜用アラビアンハート
	20050403: (14380000, 10260277), #白用アラビアンハート
	20050404: (14370000, 10260278), #黒用アラビアンハート
	#サイバーハート
	20050406: (10260000, 10260279), #桃用サイバーハート
	20050407: (10260051, 10260280), #藍用サイバーハート
	20050408: (10260050, 10260281), #緑用サイバーハート
	20050409: (10260052, 10260282), #山吹用サイバーハート
	20050410: (10260003, 10260283), #菫用サイバーハート
	20050411: (10260004, 10260284), #茜用サイバーハート
	20050412: (10260005, 10260285), #杏用サイバーハート
	20050413: (10260006, 10260286), #空用サイバーハート
	20050414: (14240000, 10260287), #胡桃用サイバーハート
	20050415: (14240000, 10260288), #若菜用サイバーハート
	20050416: (14380000, 10260289), #白用サイバーハート
	20050417: (14370000, 10260290), #黒用サイバーハート
	#ワンダーハート
	20050419: (10260000, 10260291), #桃用ワンダーハート
	20050420: (10260051, 10260292), #藍用ワンダーハート
	20050421: (10260050, 10260293), #緑用ワンダーハート
	20050422: (10260052, 10260294), #山吹用ワンダーハート
	20050423: (10260003, 10260295), #菫用ワンダーハート
	20050424: (10260004, 10260296), #茜用ワンダーハート
	20050425: (10260005, 10260297), #杏用ワンダーハート
	20050426: (10260006, 10260298), #空用ワンダーハート
	20050427: (14240000, 10260299), #胡桃用ワンダーハート
	20050428: (14240000, 10260300), #若菜用ワンダーハート
	20050429: (14380000, 10260301), #白用ワンダーハート
	20050430: (14370000, 10260302), #黒用ワンダーハート
	#ノスタルジアハート
	20050432: (10260000, 10260303), #桃用ノスタルジアハート
	20050433: (10260051, 10260304), #藍用ノスタルジアハート
	20050434: (10260050, 10260305), #緑用ノスタルジアハート
	20050435: (10260052, 10260306), #山吹用ノスタルジアハート
	20050436: (10260003, 10260307), #菫用ノスタルジアハート
	20050437: (10260004, 10260308), #茜用ノスタルジアハート
	20050438: (10260005, 10260309), #杏用ノスタルジアハート
	20050439: (10260006, 10260310), #空用ノスタルジアハート
	20050440: (14240000, 10260311), #胡桃用ノスタルジアハート
	20050441: (14240000, 10260312), #若菜用ノスタルジアハート
	20050442: (14380000, 10260313), #白用ノスタルジアハート
	20050443: (14370000, 10260314), #黒用ノスタルジアハート
	#プリティフリルハート
	20050445: (10260000, 10260315), #桃用プリティフリルハート
	20050446: (10260051, 10260316), #藍用プリティフリルハート
	20050447: (10260050, 10260317), #緑用プリティフリルハート
	20050448: (10260052, 10260318), #山吹用プリティフリルハート
	20050449: (10260003, 10260319), #菫用プリティフリルハート
	20050450: (10260004, 10260320), #茜用プリティフリルハート
	20050451: (10260005, 10260321), #杏用プリティフリルハート
	20050452: (10260006, 10260322), #空用プリティフリルハート
	20050453: (14240000, 10260323), #胡桃用プリティフリルハート
	20050454: (14240000, 10260324), #若菜用プリティフリルハート
	20050455: (14380000, 10260325), #白用プリティフリルハート
	20050456: (14370000, 10260326), #黒用プリティフリルハート
	#エクソシストハート
	20050458: (10260000, 10260327), #桃用エクソシストハート
	20050459: (10260051, 10260328), #藍用エクソシストハート
	20050460: (10260050, 10260329), #緑用エクソシストハート
	20050461: (10260052, 10260330), #山吹用エクソシストハート
	20050462: (10260003, 10260331), #菫用エクソシストハート
	20050463: (10260004, 10260332), #茜用エクソシストハート
	20050464: (10260005, 10260333), #杏用エクソシストハート
	20050465: (10260006, 10260334), #空用エクソシストハート
	20050466: (14240000, 10260335), #胡桃用エクソシストハート
	20050467: (14240000, 10260336), #若菜用エクソシストハート
	20050468: (14380000, 10260337), #白用エクソシストハート
	20050469: (14370000, 10260338), #黒用エクソシストハート
	#スチームパンクハート
	20050471: (10260000, 10260339), #桃用スチームパンクハート
	20050472: (10260051, 10260340), #藍用スチームパンクハート
	20050473: (10260050, 10260341), #緑用スチームパンクハート
	20050474: (10260052, 10260342), #山吹用スチームパンクハート
	20050475: (10260003, 10260343), #菫用スチームパンクハート
	20050476: (10260004, 10260344), #茜用スチームパンクハート
	20050477: (10260005, 10260345), #杏用スチームパンクハート
	20050478: (10260006, 10260346), #空用スチームパンクハート
	20050479: (14240000, 10260347), #胡桃用スチームパンクハート
	20050480: (14240000, 10260348), #若菜用スチームパンクハート
	20050481: (14380000, 10260349), #白用スチームパンクハート
	20050482: (14370000, 10260350), #黒用スチームパンクハート
	#フェイブルハート
	20050484: (10260000, 10260351), #桃用スチームパンクハート
	20050485: (10260051, 10260352), #藍用スチームパンクハート
	20050486: (10260050, 10260353), #緑用スチームパンクハート
	20050487: (10260052, 10260354), #山吹用スチームパンクハート
	20050488: (10260003, 10260355), #菫用スチームパンクハート
	20050489: (10260004, 10260356), #茜用スチームパンクハート
	20050490: (10260005, 10260357), #杏用スチームパンクハート
	20050491: (10260006, 10260358), #空用スチームパンクハート
	20050492: (14240000, 10260359), #胡桃用スチームパンクハート
	20050493: (14240000, 10260360), #若菜用スチームパンクハート
	20050494: (14380000, 10260361), #白用スチームパンクハート
	20050495: (14370000, 10260362), #黒用スチームパンクハート
	#ウィッチハート
	20050497: (10260000, 10260363), #桃用ウィッチハート
	20050498: (10260051, 10260364), #藍用ウィッチハート
	20050499: (10260050, 10260365), #緑用ウィッチハート
	20050500: (10260052, 10260366), #山吹用ウィッチハート
	20050501: (10260003, 10260367), #菫用ウィッチハート
	20050502: (10260004, 10260368), #茜用ウィッチハート
	20050503: (10260005, 10260369), #杏用ウィッチハート
	20050504: (10260006, 10260370), #空用ウィッチハート
	20050505: (14240000, 10260371), #胡桃用ウィッチハート
	20050506: (14240000, 10260372), #若菜用ウィッチハート
	20050507: (14380000, 10260373), #白用ウィッチハート
	20050508: (14370000, 10260374), #黒用ウィッチハート
	#バトラーハート
	20050510: (10260000, 10260375), #桃用バトラーハート
	20050511: (10260051, 10260376), #藍用バトラーハート
	20050512: (10260050, 10260377), #緑用バトラーハート
	20050513: (10260052, 10260378), #山吹用バトラーハート
	20050514: (10260003, 10260379), #菫用バトラーハート
	20050515: (10260004, 10260380), #茜用バトラーハート
	20050516: (10260005, 10260381), #杏用バトラーハート
	20050517: (10260006, 10260382), #空用バトラーハート
	20050518: (14240000, 10260383), #胡桃用バトラーハート
	20050519: (14240000, 10260384), #若菜用バトラーハート
	20050520: (14380000, 10260385), #白用バトラーハート
	20050521: (14370000, 10260386), #黒用バトラーハート
	#桃
	20050147: (10260000, 10260065), #ネコマタ（桃）用おでかけパーカー
	20050191: (10260000, 10260086), #ネコマタ（桃）用メイド服
	20050138: (10260000, 10260058), #ネコマタ（桃）キティラー服
	#緑
	20050141: (10260050, 10260059), #ネコマタ（緑）用カントリー服
	20050156: (10260050, 10260070), #ネコマタ（緑）用戦闘制服
	#藍
	20050136: (10260051, 10260057), #ネコマタ（藍）用羽衣
	20050151: (10260051, 10260054), #ネコマタ（藍）用黒セーラー
	20050179: (10260051, 10260085), #ネコマタ（藍）用リボンワンピース
	#山吹
	20050143: (10260052, 10260061), #ネコマタ（山吹）用和装
	20050178: (10260052, 10260084), #ネコマタ（山吹）用ボーイッシュ服
	#菫
	20050146: (10260003, 10260064), #ネコマタ（菫）用おめかしワンピ
	20050158: (10260003, 10260071), #ネコマタ（菫）用着物ワンピ
	#茜
	20050144: (10260004, 10260062), #ネコマタ（茜）用ハロウィン服
	20050150: (10260004, 10260066), #ネコマタ（茜）用チャイナドレス
	#杏
	20050130: (10260005, 10260056), #ネコマタ（杏）用セーラー
	20050152: (10260005, 10260067), #ネコマタ（杏）用エルブンジャケット
	#空
	20050145: (10260006, 10260063), #ネコマタ（空）用怪盗服
	20050154: (10260006, 10260069), #ネコマタ（空）用さざなみのワンピース
	#胡桃・若菜
	20050149: (14240000, 14240002), #ネコマタ（胡桃・若菜）用メイド服
	20050134: (14240000, 14240001), #ネコマタ（胡桃・若菜）用水着
	20050166: (14240000, 10260073), #ネコマタ(胡桃・若菜)用カボチャマント
	#白
	20050142: (14380000, 10260060), #ネコマタ（白）用トップモデル服
	20050153: (14380000, 10260068), #ネコマタ（白）用ウェディングドレス
	20050168: (14380000, 10260075), #ネコマタ（白）用カボチャマント
	#黒
	20050131: (14370000, 14370001), #ネコマタ（黒）用騎士服
	20050148: (14370000, 14370002), #ネコマタ（黒）用巫女服
	20050167: (14370000, 10260074), #ネコマタ（黒）用カボチャマント
	20050534: (14370000, 14370003), #ネコマタ（黒）用舞踏会ドレス
	#etc
	20050169: (14760000, 10260076), #ネコマタ（ミケ）用カボチャマント
	20050170: (14810000, 10260077), #ネコマタ（トラ）用カボチャマント
	20050171: (15280000, 10260078), #ネコマタ（アリス）用カボチャマント
	#オートマタ
	20050172: (14900000, 10260079), #アメジスト用カボチャマント
	20050173: (14940000, 10260080), #ルビー用カボチャマント
	20050174: (14960000, 10260081), #トパーズ用カボチャマント
	20050175: (15240000, 10260082), #サファイア用カボチャマント
	20050176: (15310000, 10260083), #ダイヤモンド用カボチャマント
	#シモツキ用フェイブルハート（白）
	10136301: (19010112, 19010113), #シモツキ用フェイブルハート（白）
}

def main(pc):
	nekomata_info = ITEM_EVENT_ID[pc.item_event_id]
	if not pc.pet:
		script.msg(pc, "error: not pet")
		return
	with pc.lock and pc.pet.lock:
		pet_item = pc.item.get(pc.equip.pet)
		if not pet_item:
			script.msg(pc, "error: not pet equip")
			return
		if pet_item.pet_id != nekomata_info[0]:
			script.msg(pc, "error: pet id != %s"%nekomata_info[0])
			return
		if pc.pet.item[1].pict_id == nekomata_info[1]:
			pet_pict_id = nekomata_info[0]
		else:
			pet_pict_id = nekomata_info[1]
		pet_item.pet_pict_id = pet_pict_id
		pc.pet.item[1].pict_id = pet_pict_id
		script.update_pet(pc)