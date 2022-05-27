#
# Müəllif hüququ (C) 2021-2022, TeamYukki@Github, < https://github.com/TeamYukki >.
#
# Bu fayl < https://github.com/TeamYukki/YukkiMusicBot > layihəsinin bir hissəsidir,
# və "GNU v3.0 Lisenziya Müqaviləsi" əsasında buraxılır.
# Zəhmət olmasa baxın < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# Bütün hüquqlar qorunur.

HELP_1 = """✅**<u>Admin Əmrləri:</u>**
**c** kanal oyunu qurmaq.
/pause və ya /cpause - Oxunan musiqini dayandırın.
/resume və ya /cresume- Pauza edilmiş musiqini davam etdirin.
/sessiz və ya /cmute- Oynanan musiqinin səsini söndürün.
/unmute və ya /cunmute- Səssiz musiqinin səsini açın.
/skip və ya /cskip- Cari ifa olunan musiqini keçin.
/stop və ya /cstop- Oynanan musiqini dayandırın.
/shuffle və ya /cshuffle- Növbəyə qoyulmuş pleylistləri təsirə məruz qoyub.
/seek və ya /cseek - İrəli Musiqini yaxınlarınıza qədər axtarın
/seekback və ya /cseekback - Geriyə Musiqini yaxınlarınıza qədər axtarın
/yenidən başladın - Söhbətiniz üçün botu yenidən başladın.
✅<u>**Xüsusi keçid:**</u>
/skip və ya /cskip [Nömrə(misal: 3)]
    - Musiqini seçilmiş növbəli nömrəyə keçir. Nümunə: /skip 3 musiqini üçüncü musiqiyə keçirəcək və növbə olan 1 və 2 musiqiyə məhəl qoymayacaq.
✅<u>**Loop Play:**</u>
/loop və ya /clop [enable/disable] və ya [1-10 arası rəqəmlər]
    - Aktivləşdirilir, bot səsli söhbətdə cari ifa olunan musiqini 1-10 dəfə çevirir. Varsayılan olaraq 10 dəfə.
✅<u>**Auth İstifadəçiləri:**</u>
Auth İstifadəçiləri söhbətinizdə admin hüquqları olmadan admin əmrindən istifadə edə bilərsiniz.
/auth [İstifadəçi adı] - Qrupun AUTH SİYAHISINA əlavə edin.
/unauth [İstifadəçi adı] - Qrupun AUTH LIST-dən istifadəçini çıxarın.
/authusers - Qrupun AUTH SİYAHISINI yoxlayın."""


HELP_2 = """✅<u>**Oynatma Əmrləri:**</u>

Mövcud Əmrlər = play , vplay , cplay

ForcePlay Əmrləri = playforce , vplayforce , cplayforce

**c** kanal oyunu deməkdir.
**v** video oynatma deməkdir.
**force** güc oyunu deməkdir.

/play və ya /vplay və ya /cplay - Bot verdiyiniz sorğunu səsli söhbətdə oynamağa başlayacaq və ya səsli söhbətlərdə canlı bağlantıları yayımlayacaq.

/playforce və ya /vplayforce və ya /cplayforce - **Force Play** səsli çatda cari ifa olunan treki dayandırır və növbəni pozmadan/təmizləmədən axtarılan treki dərhal ifa etməyə başlayır.

/channelplay [Söhbət istifadəçi adı və ya id] və ya [Disable] - Kanalı qrupa qoşun və qrupunuzdan kanalın səsli söhbətində musiqi yayımlayın.


✅**<u>Botun Server Pleylistləri:</u>**
/playlist - Serverlərdə Saxlanmış Pleylistinizi yoxlayın.
/deleteplaylist - Pleylistinizdə saxlanan hər hansı musiqini silin
/play - Serverlərdən Saxlanmış Pleylistinizi oynatmağa başlayın."""


HELP_3 = """✅<u>**Bot Əmrləri:**</u>

/stats - Qlobal Statistikanın ən yaxşı 10 trekini, botun ən yaxşı 10 istifadəçisini, botda ən yaxşı 10 söhbəti, söhbətdə oynanan ən yaxşı 10-u və s. alın.

/sudolist - Yukki Musiqi Botunun Sudo İstifadəçilərini yoxlayın

/lyrics [Musiqi Adı] - Vebdə xüsusi Musiqi üçün Lirikləri axtarır.

/mahnı [Track Name] və ya [YT Link] - YouTube-dan mp3 və ya mp4 formatında istənilən treki yükləyin.

/player - İnteraktiv Oyun Paneli əldə edin.

**c** kanal oyunu deməkdir.

/queue və ya /cqueue- Musiqinin Növbə Siyahısını yoxlayın."""

HELP_4 = """✅<u>**Əlavə Əmrlər:**</u>
/start - Musiqi Botunu işə salın.
/ help - Əmrlərin ətraflı izahı ilə Əmrlər Köməkçisi Menyusunu əldə edin.
/ping- Botu pingləyin və Botun Ram, CPU və s. statistikasını yoxlayın.

✅<u>**Qrup Parametrləri:**</u>
/parametrlər - Daxili düymələrlə tam qrupun parametrlərini əldə edin

🔗 **Parametrlərdəki seçimlər:**

1️⃣ Siz səsli söhbətdə yayımlamaq istədiyiniz **Audio Keyfiyyətini** təyin edə bilərsiniz.

2️⃣ Siz səsli söhbətdə yayımlamaq istədiyiniz **Video Keyfiyyətini** təyin edə bilərsiniz.

3️⃣ **Auth Users**:- Admin əmrləri rejimini buradan hamıya və ya yalnız adminlərə dəyişə bilərsiniz. Əgər hər kəs, sizin qrupunuzda olan hər kəs admin əmrlərindən istifadə edə biləcək (məsələn, /skip, /stop və s.)

4️⃣ **Təmiz rejimi:** Söhbətinizin təmiz və yaxşı qaldığından əmin olmaq üçün aktivləşdirildikdə botun mesajlarını 5 dəqiqədən sonra qrupunuzdan silir.

5️⃣ **Command Clean** : Aktivləşdirildikdə, Bot icra etdiyi əmrləri (/oynat, /pauza, /qarışdır, /dayan və s.) dərhal siləcək.

6️⃣ **Oynatma Parametrləri:**

/playmode - Qrupunuzun oyun parametrlərini təyin edə biləcəyiniz düymələri olan tam oyun parametrləri paneli əldə edin.

<u>Oyun rejimində seçimlər:</u>

1️⃣ **Axtarış Modu** [Birbaşa və ya Daxil] - Siz /oyun rejimini verərkən axtarış rejiminizi dəyişir.

2️⃣ **Admin Əmrləri** [Hər kəs və ya Adminlər] - Qrupunuzda olan hər kəs admin əmrlərindən (/skip, /stop və s.) istifadə edə bilər.

3️⃣ **Oynatma Növü** [Hər kəs və ya Adminlər] - Adminlərsə, yalnız qrupda olan adminlər səsli çatda musiqi oxuya bilər."""

HELP_5 = """🔰**<u>SUDO İSTİFADƏÇİLƏRİNİ ƏLAVƏ EDİN və SİLİN :</u>**
/addsudo [İstifadəçi adı və ya istifadəçiyə cavab]
/delsudo [İstifadəçi adı və ya istifadəçiyə cavab]

🛃**<u>HEROKU:</u>**
/istifadə - Dyno İstifadəsi.

🌐**<u>VARS KONFIQLƏMƏ:</u>**
/get_var - Heroku və ya .env-dən konfiqurasiya var əldə edin.
/del_var - Heroku və ya .env-də istənilən varı silin.
/set_var [Var Adı] [Dəyər] - Heroku və ya .env-də Var təyin edin və ya Varı yeniləyin. Var və onun dəyərini boşluqla ayırın.

🤖**<u>BOT ƏMƏRLƏRİ:</u>**
/reboot - Botunuzu yenidən başladın.
/ yeniləmə - Botu yeniləyin.
/speedtest - Server sürətlərini yoxlayın
/ baxım [aktiv / söndürün]
/logger [enable / disable] - Bot axtarış edilmiş sorğuları qeydiyyatçı qrupunda qeyd edir.
/get_log [Xətlərin sayı] - Heroku və ya vps-dən botunuzun qeydini əldə edin. Hər ikisi üçün işləyir.
/autoend [enable|disable] - Heç kim qulaq asmırsa, 3 dəqiqədən sonra avtomatik axın sonunu aktivləşdirin.

📈**<u>STATİS ƏMRLARI:</u>**
/activevoice - Botda aktiv səsli söhbətləri yoxlayın.
/activevideo - Botda aktiv video zəngləri yoxlayın.
/stats - Botların Statistikasını yoxlayın

⚠️**<u>QARA SİYAHİ SAHİB FUNKSİYASI:</u>**
/blacklistchat [CHAT_ID] - Musiqi Botundan istifadə etməklə bağlı istənilən söhbəti qara siyahıya salın
/whitelistchat [CHAT_ID] - Musiqi Botundan istifadə etmək üçün qara siyahıya alınmış hər hansı söhbəti ağ siyahıya daxil edin
/blacklistedchat - Bütün qara siyahıya alınmış söhbətləri yoxlayın.

👤**<u>Bloklanmış funksiya:</u>**
/block [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçinin bot əmrlərindən istifadəsinin qarşısını alır.
/blokdan çıxart [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçini Botun Bloklanmış Siyahısından çıxarın.
/blockedusers - Bloklanmış İstifadəçi Siyahılarını yoxlayın

👤**<u>GBAN FUNKSİYASI:</u>**
/gban [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçini botun xidmət etdiyi çatdan bloklayın və onun botunuzdan istifadəsini dayandırın.
/ungban [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçini Botun qadağan olunmuş Siyahısından çıxarın və ona botunuzdan istifadə etməyə icazə verin
/gbannedusers - Gbanned İstifadəçi Siyahılarını yoxlayın

🎥**<u>VİDEOKALLAR FONKSİYASI:</u>**
/set_video_limit [Söhbətlərin Sayı] - Eyni anda Video Zənglər üçün icazə verilən Söhbətlərin maksimum sayını təyin edin. Defolt olaraq 3 söhbət.
/videomode [download|m3u8] - Yükləmə rejimi aktivdirsə, Bot videoları M3u8 formasında oynamaq əvəzinə endirəcək. Varsayılan olaraq M3u8-ə. Hər hansı sorğu m3u8 rejimində oxunmayanda yükləmə rejimindən istifadə edə bilərsiniz.

⚡️**<u>ŞƏXSİ BOT FUNKSİYASI:</u>**
/authorize [CHAT_ID] - Botunuzdan istifadə etmək üçün söhbətə icazə verin.
/unauthorize [CHAT_ID] - Çata botunuzdan istifadə etməyə icazə verməyin.
/səlahiyyətli - Botunuzun bütün icazə verilən söhbətlərini yoxlayın.

🌐**<u>YAYIM FONKSİYASI:</u>**
/yayım [Mesaj və ya Mesaja Cavab] - Botun Xidmət edilən Çatlarına istənilən mesajı yayımlayın.

<u>yayım seçimləri:</u>
**-pin** : Bu, mesajınızı sancacaq
**-pinloud**: Bu, mesajınızı yüksək səslə bildirişlə bağlayacaq
**-user** : Bu, mesajınızı botunuzu işə salmış istifadəçilərə yayımlayacaq.
**-köməkçi** : Bu, mesajınızı botunuzun köməkçi hesabından yayımlayacaq.
**-nobot** : Bu, botunuzu mesaj yayımlamamağa məcbur edəcək

**Misal:** `/yayım -istifadəçi -köməkçi -pin Salam Testi`

"""
