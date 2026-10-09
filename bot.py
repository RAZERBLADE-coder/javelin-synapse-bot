from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import os

# =========================================================
# BOT TOKEN
# =========================================================

TOKEN = "os.environ["BOT_TOKEN"]"


# =========================================================
# TEXTS
# =========================================================

TEXTS = {

    # =====================================================
    # UZBEK
    # =====================================================

    "uz": {

        "greeting": "Assalomu alaykum",

        "welcome": "JΛVΞLIN SYNAPSE ⚡ ga xush kelibsiz.",

        "description": (
            "Bu yerda JAVELIN haqida, uning ko‘nikmalari, "
            "loyihalari va raqamli faoliyati haqida "
            "ma’lumot olishingiz mumkin."
        ),

        "choose": "✦ Kerakli bo‘limni tanlang",

        "about": "👤 Men haqimda",
        "skills": "🧠 Ko‘nikmalar",
        "projects": "💻 Loyihalar",
        "telegram": "✈️ Telegram kanal",
        "social": "🌐 Ijtimoiy tarmoqlar",
        "vision": "◈ Kelajak",

        "back": "← Orqaga",

        "uz": "🇺🇿 O‘zbek",
        "en": "🇬🇧 English",
        "ru": "🇷🇺 Русский",

        # -------------------------------------------------
        # UNDER CONSTRUCTION
        # -------------------------------------------------

        "under_construction": (
            "🚧 Bu bo‘lim hozircha ishlab chiqilmoqda."
        ),

        # -------------------------------------------------
        # ABOUT
        # -------------------------------------------------

        "about_text": """
👨‍💻 *MEN HAQIMDA*

💻 *FULL-STACK DEVELOPER*

Web texnologiyalari va dasturlashga qiziqaman. Frontend va backend yo‘nalishlarida ishlash, zamonaviy va interaktiv loyihalar yaratish hamda o‘z g‘oyalarimni real mahsulotlarga aylantirishni yoqtiraman.

⚙️ *C++ & PYTHON DEVELOPER*

C++ va Python dasturlash tillari bilan shug‘ullanaman. Algoritmlar, dasturiy yechimlar va turli loyihalar orqali dasturlash bo‘yicha bilimlarimni rivojlantirib boraman.

🎮 *GAME CREATOR & DESIGNER*

Gaming men uchun shunchaki o‘yin o‘ynash emas — yaratish jarayoniga ham katta qiziqaman. Roblox, Minecraft va boshqa platformalarda o‘yinlar yaratish, 3D obyektlar va turli vizual elementlarni loyihalash bilan shug‘ullanganman.

🎥 *GAMER & CONTENT CREATOR*

Gaming va kontent yaratishni birlashtiraman. Roblox, Mech Arena, Minecraft va Steam o‘yinlarini o‘ynayman hamda YouTube va Instagram uchun video kontentlar yaratib boraman.

🚀 *MAQSADIM*

Dasturlash, texnologiya, gaming va kreativlikdagi bilimlarimni birlashtirib, o‘z kompaniyam — *JΛVΞLIN* —ni rivojlantirish.

JΛVΞLIN kelajakda CPU, GPU va boshqa zamonaviy texnologiyalar yo‘nalishida faoliyat yurituvchi texnologik kompaniyaga aylanishi mening katta maqsadlarimdan biridir.

Doimiy o‘rganish, yaratish va rivojlanish — mening asosiy yo‘nalishim.

✦ *Powered By JΛVΞLIN Synapse⚡️* ✦
""",

        # -------------------------------------------------
        # SKILLS
        # -------------------------------------------------

        "skills_text": """
🧠 *KO‘NIKMALARIM*

🌐 *WEB DEVELOPMENT & DESIGN*

HTML • CSS • JavaScript • Figma

Zamonaviy web-interfeyslar, responsive dizayn va interaktiv sahifalar yaratish. Dizayn g‘oyasini Figma orqali shakllantirib, uni ishlaydigan web-interfeysga aylantirish.

🎨 *UI/UX DEVELOPMENT*

React.js • TypeScript

Foydalanuvchi interfeyslarini yaratish, komponentlarga asoslangan web-ilovalar ishlab chiqish va qulay user experience uchun zamonaviy yechimlardan foydalanish.

🎮 *GAME SCRIPTING & DESIGN*

C++ • Unreal Engine • 3D Design

O‘yin mexanikalari, gameplay logikasi va 3D muhitlar yaratishga qiziqish. Unreal Engine va C++ orqali game development yo‘nalishini rivojlantirish.

⚙️ *CPU & GPU ARCHITECTURE*

Computer Architecture • Digital Logic • Verilog/SystemVerilog • CUDA

Protsessor va grafik protsessorlarning ishlash prinsiplari, arxitekturasi hamda hardware va software o‘rtasidagi bog‘liqlikni o‘rganish.

✦ *Powered By JΛVΞLIN Synapse⚡️* ✦
""",
    },


    # =====================================================
    # ENGLISH
    # =====================================================

    "en": {

        "greeting": "Hello",

        "welcome": "Welcome to JΛVΞLIN SYNAPSE ⚡.",

        "description": (
            "Explore JAVELIN's profile, skills, "
            "projects and digital activity."
        ),

        "choose": "✦ Choose a section",

        "about": "👤 About Me",
        "skills": "🧠 Skills",
        "projects": "💻 Projects",
        "telegram": "✈️ Telegram Channel",
        "social": "🌐 Social Networks",
        "vision": "◈ Vision",

        "back": "← Back",

        "uz": "🇺🇿 O‘zbek",
        "en": "🇬🇧 English",
        "ru": "🇷🇺 Русский",

        # -------------------------------------------------
        # UNDER CONSTRUCTION
        # -------------------------------------------------

        "under_construction": (
            "🚧 This section is currently under construction."
        ),

        # -------------------------------------------------
        # ABOUT
        # -------------------------------------------------

        "about_text": """
👨‍💻 *ABOUT ME*

💻 *FULL-STACK DEVELOPER*

I’m passionate about web technologies and software development. I work across both frontend and backend, enjoy building modern and interactive projects, and turning my ideas into real-world products.

⚙️ *C++ & PYTHON DEVELOPER*

I work with C++ and Python, continuously developing my programming skills through algorithms, software solutions, and various projects.

🎮 *GAME CREATOR & DESIGNER*

Gaming is more than just playing for me — I’m also interested in the creative and development side of it. I’ve worked on game creation, 3D objects, and various visual elements for platforms such as Roblox and Minecraft.

🎥 *GAMER & CONTENT CREATOR*

I combine gaming with content creation. I play Roblox, Mech Arena, Minecraft, and games on Steam, while also creating video content for YouTube and Instagram.

🚀 *MY GOAL*

To combine my knowledge of programming, technology, gaming, and creativity to develop my own company — *JΛVΞLIN*.

In the future, I aim to develop JΛVΞLIN into a technology company focused on CPUs, GPUs, and other advanced technologies.

Continuous learning, creating, and improving are the core principles of my journey.

✦ *Powered By JΛVΞLIN Synapse⚡️* ✦
""",

        # -------------------------------------------------
        # SKILLS
        # -------------------------------------------------

        "skills_text": """
🧠 *MY SKILLS*

🌐 *WEB DEVELOPMENT & DESIGN*

HTML • CSS • JavaScript • Figma

Creating modern web interfaces, responsive designs, and interactive pages. Turning design concepts created in Figma into functional web interfaces.

🎨 *UI/UX DEVELOPMENT*

React.js • TypeScript

Building user interfaces, developing component-based web applications, and using modern solutions to create a better user experience.

🎮 *GAME SCRIPTING & DESIGN*

C++ • Unreal Engine • 3D Design

Exploring gameplay mechanics, game logic, and 3D environments. Developing game development skills through Unreal Engine and C++.

⚙️ *CPU & GPU ARCHITECTURE*

Computer Architecture • Digital Logic • Verilog/SystemVerilog • CUDA

Exploring how processors and graphics processors work, their architecture, and the relationship between hardware and software.

✦ *Powered By JΛVΞLIN Synapse⚡️* ✦
""",
    },


    # =====================================================
    # RUSSIAN
    # =====================================================

    "ru": {

        "greeting": "Здравствуйте",

        "welcome": "Добро пожаловать в JΛVΞLIN SYNAPSE ⚡.",

        "description": (
            "Здесь вы можете узнать больше о JAVELIN, "
            "его навыках, проектах и цифровой деятельности."
        ),

        "choose": "✦ Выберите раздел",

        "about": "👤 Обо мне",
        "skills": "🧠 Навыки",
        "projects": "💻 Проекты",
        "telegram": "✈️ Telegram-канал",
        "social": "🌐 Социальные сети",
        "vision": "◈ Будущее",

        "back": "← Назад",

        "uz": "🇺🇿 O‘zbek",
        "en": "🇬🇧 English",
        "ru": "🇷🇺 Русский",

        # -------------------------------------------------
        # UNDER CONSTRUCTION
        # -------------------------------------------------

        "under_construction": (
            "🚧 Этот раздел пока находится в разработке."
        ),

        # -------------------------------------------------
        # ABOUT
        # -------------------------------------------------

        "about_text": """
👨‍💻 *ОБО МНЕ*

💻 *FULL-STACK DEVELOPER*

Я интересуюсь веб-технологиями и разработкой программного обеспечения. Работаю с frontend и backend, люблю создавать современные и интерактивные проекты и превращать свои идеи в реальные продукты.

⚙️ *C++ & PYTHON DEVELOPER*

Работаю с языками программирования C++ и Python. Постоянно развиваю свои навыки программирования через алгоритмы, программные решения и различные проекты.

🎮 *GAME CREATOR & DESIGNER*

Для меня gaming — это не только игры, но и возможность создавать что-то своё. Я интересуюсь разработкой игр, созданием 3D-объектов и различных визуальных элементов для таких платформ, как Roblox и Minecraft.

🎥 *GAMER & CONTENT CREATOR*

Я совмещаю gaming и создание контента. Играю в Roblox, Mech Arena, Minecraft и игры в Steam, а также создаю видеоконтент для YouTube и Instagram.

🚀 *МОЯ ЦЕЛЬ*

Объединить знания в области программирования, технологий, gaming и творчества и развивать собственную компанию — *JΛVΞLIN*.

В будущем я стремлюсь развить JΛVΞLIN в технологическую компанию, специализирующуюся на CPU, GPU и других современных технологиях.

Постоянно учиться, создавать и развиваться — мой основной принцип.

✦ *Powered By JΛVΞLIN Synapse⚡️* ✦
""",

        # -------------------------------------------------
        # SKILLS
        # -------------------------------------------------

        "skills_text": """
🧠 *МОИ НАВЫКИ*

🌐 *WEB-РАЗРАБОТКА И ДИЗАЙН*

HTML • CSS • JavaScript • Figma

Создание современных веб-интерфейсов, адаптивного дизайна и интерактивных страниц. Превращение дизайн-концепций из Figma в функциональные веб-интерфейсы.

🎨 *UI/UX DEVELOPMENT*

React.js • TypeScript

Создание пользовательских интерфейсов, разработка компонентных веб-приложений и использование современных решений для удобного пользовательского опыта.

🎮 *GAME SCRIPTING & DESIGN*

C++ • Unreal Engine • 3D Design

Изучение игровых механик, игровой логики и 3D-сред. Развитие навыков game development с использованием Unreal Engine и C++.

⚙️ *АРХИТЕКТУРА CPU И GPU*

Computer Architecture • Digital Logic • Verilog/SystemVerilog • CUDA

Изучение принципов работы процессоров и графических процессоров, их архитектуры и взаимосвязи между hardware и software.

✦ *Powered By JΛVΞLIN Synapse⚡️* ✦
""",
    },
}


# =========================================================
# MAIN MENU
# =========================================================

def main_menu(language, first_name):

    t = TEXTS[language]

    text = f"""
👋 *{t["greeting"]}, {first_name}!*

*{t["welcome"]}*

{t["description"]}

{t["choose"]} 👇
"""

    keyboard = [
        [
            InlineKeyboardButton(
                t["about"],
                callback_data="about"
            ),
            InlineKeyboardButton(
                t["skills"],
                callback_data="skills"
            ),
        ],
        [
            InlineKeyboardButton(
                t["projects"],
                callback_data="projects"
            ),
            InlineKeyboardButton(
                t["telegram"],
                callback_data="telegram"
            ),
        ],
        [
            InlineKeyboardButton(
                t["social"],
                callback_data="social"
            ),
            InlineKeyboardButton(
                t["vision"],
                callback_data="vision"
            ),
        ],
        [
            InlineKeyboardButton(
                t["uz"],
                callback_data="lang_uz"
            ),
            InlineKeyboardButton(
                t["en"],
                callback_data="lang_en"
            ),
            InlineKeyboardButton(
                t["ru"],
                callback_data="lang_ru"
            ),
        ],
    ]

    return text, InlineKeyboardMarkup(keyboard)


# =========================================================
# PAGE KEYBOARD
# =========================================================

def page_keyboard(language):

    t = TEXTS[language]

    keyboard = [
        [
            InlineKeyboardButton(
                t["back"],
                callback_data="home"
            )
        ],
        [
            InlineKeyboardButton(
                t["uz"],
                callback_data="lang_uz"
            ),
            InlineKeyboardButton(
                t["en"],
                callback_data="lang_en"
            ),
            InlineKeyboardButton(
                t["ru"],
                callback_data="lang_ru"
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================================================
# START
# =========================================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user

    first_name = user.first_name or "User"

    language = context.user_data.get(
        "language",
        "uz"
    )

    context.user_data["current_page"] = "home"

    text, keyboard = main_menu(
        language,
        first_name
    )

    await update.message.reply_text(
        text,
        reply_markup=keyboard,
        parse_mode="Markdown"
    )


# =========================================================
# BUTTON HANDLER
# =========================================================

async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    data = query.data

    current_page = context.user_data.get(
        "current_page",
        "home"
    )


    # =====================================================
    # LANGUAGE SWITCH
    # =====================================================

    if data.startswith("lang_"):

        language = data.replace(
            "lang_",
            ""
        )

        old_language = context.user_data.get(
            "language",
            "uz"
        )

        context.user_data["language"] = language


        # -------------------------------------------------
        # ABOUT -> yangi til
        # -------------------------------------------------

        if current_page == "about":

            await query.edit_message_text(
                TEXTS[language]["about_text"],
                reply_markup=page_keyboard(language),
                parse_mode="Markdown"
            )

            return


        # -------------------------------------------------
        # SKILLS -> yangi til
        # -------------------------------------------------

        if current_page == "skills":

            await query.edit_message_text(
                TEXTS[language]["skills_text"],
                reply_markup=page_keyboard(language),
                parse_mode="Markdown"
            )

            return


        # -------------------------------------------------
        # UNDER CONSTRUCTION PAGE -> yangi til
        # -------------------------------------------------

        if current_page in [
            "projects",
            "telegram",
            "social",
            "vision"
        ]:

            t = TEXTS[language]

            section_name = {
                "projects": t["projects"],
                "telegram": t["telegram"],
                "social": t["social"],
                "vision": t["vision"],
            }[current_page]

            text = f"""
*{section_name}*

━━━━━━━━━━━━━━━━━━

{t["under_construction"]}

✦ *Powered By JΛVΞLIN Synapse⚡️* ✦
"""

            await query.edit_message_text(
                text,
                reply_markup=page_keyboard(language),
                parse_mode="Markdown"
            )

            return


        # -------------------------------------------------
        # HOME -> yangi til
        # -------------------------------------------------

        user = update.effective_user

        first_name = user.first_name or "User"

        text, keyboard = main_menu(
            language,
            first_name
        )

        await query.edit_message_text(
            text,
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

        return


    # =====================================================
    # ABOUT
    # =====================================================

    if data == "about":

        language = context.user_data.get(
            "language",
            "uz"
        )

        context.user_data["current_page"] = "about"

        await query.edit_message_text(
            TEXTS[language]["about_text"],
            reply_markup=page_keyboard(language),
            parse_mode="Markdown"
        )

        return


    # =====================================================
    # SKILLS
    # =====================================================

    if data == "skills":

        language = context.user_data.get(
            "language",
            "uz"
        )

        context.user_data["current_page"] = "skills"

        await query.edit_message_text(
            TEXTS[language]["skills_text"],
            reply_markup=page_keyboard(language),
            parse_mode="Markdown"
        )

        return


    # =====================================================
    # OTHER SECTIONS
    # =====================================================

    if data in [
        "projects",
        "telegram",
        "social",
        "vision"
    ]:

        language = context.user_data.get(
            "language",
            "uz"
        )

        context.user_data["current_page"] = data

        t = TEXTS[language]

        section_name = {
            "projects": t["projects"],
            "telegram": t["telegram"],
            "social": t["social"],
            "vision": t["vision"],
        }[data]

        text = f"""
*{section_name}*

━━━━━━━━━━━━━━━━━━

{t["under_construction"]}

✦ *Powered By JΛVΞLIN Synapse⚡️* ✦
"""

        await query.edit_message_text(
            text,
            reply_markup=page_keyboard(language),
            parse_mode="Markdown"
        )

        return


    # =====================================================
    # HOME
    # =====================================================

    if data == "home":

        language = context.user_data.get(
            "language",
            "uz"
        )

        context.user_data["current_page"] = "home"

        user = update.effective_user

        first_name = user.first_name or "User"

        text, keyboard = main_menu(
            language,
            first_name
        )

        await query.edit_message_text(
            text,
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

        return


# =========================================================
# RUN BOT
# =========================================================

app = Application.builder().token(TOKEN).build()

app.add_handler(
    CommandHandler(
        "start",
        start
    )
)

app.add_handler(
    CallbackQueryHandler(
        button_handler
    )
)

print("✦ JΛVΞLIN SYNAPSE ⚡ IS ONLINE ✦")

app.run_polling()
