import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS for language selector - add before </style>
lang_css = '''
/* LANGUAGE SELECTOR */
#lang-dropdown{position:absolute;top:10px;right:20px;z-index:100}
#lang-btn{background:rgba(10,18,42,.9);border:1px solid rgba(50,80,130,.7);color:rgba(200,168,75,.9);font-size:1.2rem;padding:8px 14px;border-radius:8px;cursor:pointer;display:flex;align-items:center;gap:6px;transition:all .2s}
#lang-btn:hover{background:rgba(20,35,65,.95);border-color:rgba(200,168,75,.5)}
.lang-arrow{font-size:.6rem;color:rgba(180,195,215,.6);transition:transform .2s}
#lang-dropdown.open .lang-arrow{transform:rotate(180deg)}
#lang-menu{display:none;position:absolute;top:calc(100% + 8px);right:0;background:rgba(10,18,42,.98);border:1px solid rgba(50,80,130,.7);border-radius:10px;min-width:150px;box-shadow:0 8px 32px rgba(0,0,0,.6);overflow:hidden}
#lang-dropdown.open #lang-menu{display:block}
.lang-option{padding:12px 16px;font-size:.85rem;color:rgba(200,210,230,.85);cursor:pointer;display:flex;align-items:center;gap:10px;transition:background .15s}
.lang-option:hover{background:rgba(30,50,90,.8);color:rgb(232,228,217)}
.lang-option.active{background:rgba(200,168,75,.15);color:rgb(200,168,75)}
@media(max-width:768px){#lang-dropdown{top:10px;right:12px}}
'''

# Insert CSS before </style>
content = content.replace('</style>', lang_css + '\n</style>')

# HTML for language selector - add after <div id="header">
lang_html = '''
<div id="lang-dropdown">
  <button id="lang-btn" onclick="toggleLangDropdown(event)">🇺🇸 <span class="lang-arrow">▼</span></button>
  <div id="lang-menu">
    <div class="lang-option" onclick="selectLang('en')">🇺🇸 English</div>
    <div class="lang-option" onclick="selectLang('pt')">🇧🇷 Português</div>
    <div class="lang-option" onclick="selectLang('es')">🇪🇸 Español</div>
    <div class="lang-option" onclick="selectLang('tr')">🇹🇷 Türkçe</div>
  </div>
</div>
'''

# Insert after <div id="header">
content = content.replace('<div id="header">', '<div id="header">\n' + lang_html)

# Read the JS file
with open('language-selector.js', 'r', encoding='utf-8') as f:
    lang_js = f.read()

# Insert JS before </script> (before the closing of the main script)
# Find the last </script> and insert before it
last_script_pos = content.rfind('</script>')
if last_script_pos != -1:
    # Find the opening of this script
    script_start = content.rfind('<script>', 0, last_script_pos)
    if script_start != -1:
        # Get the existing script content
        existing_script = content[script_start+8:last_script_pos]
        # Add our code at the end of the existing script
        new_script = '<script>\n' + lang_js + '\n' + existing_script + '</script>'
        content = content[:script_start] + new_script + content[last_script_pos+9:]

# Write the modified file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Language selector added successfully!")
