import os
import re

# Der HTML/JS-Inhalt direkt als String im Skript hinterlegt
html_content = """
<div class="container">
<h2>SQL Info</h2>

<select id="queryType" onchange="updateTopics()">
    <option value="select">SELECT</option>
    <option value="DA_SPK">DA_SPK</option>
    <option value="Sys_admin">Sys_admin</option>
    <option value="update">UPDATE</option>
    <option value="delete">DELETE</option>
    <option value="create">CREATE</option>
    <option value="wortschatz">WORTSCHATZ</option>
</select>

<select id="topic"></select>
<button onclick="showExample()">Suchen</button>
<div class="result" id="example"></div>
</div>

<script>
const topics = {
    select: {
        "EXTRACT": `EXTRACT(часть_даты FROM дата_или_время)\n\nЧасти даты/времени:\n\nYEAR    – год\nMONTH   – месяц\nDAY     – день\nHOUR    – час\nMINUTE  – минута\nSECOND  – секунда\n\n::date / ::time/ ::text - во что превратить значение по итогу\n\nПримеры:\n\n-- Получить год из даты\nSELECT EXTRACT(YEAR FROM '2026-02-23'::date);\n\n-- Можно использовать с CURRENT_DATE / _TIMESTAMP\n\nSELECT EXTRACT(YEAR FROM CURRENT_DATE);\nSELECT EXTRACT(HOUR FROM CURRENT_TIMESTAMP)\n\n--Математика, сравнения, агрегаты и т.д.\nSELECT EXTRACT(YEAR FROM '2026-02-23') + 1; -- 2027`,
        "to_char": `\nvon Zahlen oder Datum zu TEXT\n\nBeispiel -\nto_char(pe.geburtsdatum, 'DD.MM.YYYY') as geburtsdatum\n\n`,
        "::": `\n\nBeispiel -\nSelect '123'::int\nAus - 123 Zahlen\n\n`,
        "SUBSTR": `\n(WAS, ab welche Zeichen, wie viel Zeichen zu nehmen)\n\nSELECT SUBSTR('HELLO',1,2)\n\nAusgabe -'HE'\n\nBeispiel - \nwhere substr(p1.oe, 6, 2) not in ('04', '06')\n\n`
    },
    DA_SPK: {
        "Import_Anleitung": `\n<b>1. Erstellen wir eine Tabelle</b>\n   Wichtig - Begriffe von Zeile ohne leere Platz bevor Begriff\n\n<b>2. da_selects</b> \n   suchen wir datei - DA_einmalig_VC\n   dort anpassen Name - datei=glpi_test\n	                tabelle=TEMP.glpi_test\n   speichern\n\n<b>3.P:\\DA-Import\\ORG-EDV-DM</b>\n  Kopieren wir unsere tabelle hier and warten bis Verschwinden der Tabelle\n\n<b>4.Uberprüfen</b>, ob zusätzliche File in da-select mit Name da_einmalig_VC_FEHLER   nicht entsteht`,
        "Export Tabelle zur Kollegen": `\n1. drop table if exists TEMP.aw12364_1;\ncreate table TEMP.aw12364_1 as (\n\nSQL_CODE SQL_CODE SQL_CODE SQL_CODE SQL_CODE\n\n) with data\n;\n\n2.Code durchführen, um Tabellen zu erstellen\n\n3. da_selects\nmein Datei - DA_einmalig_VC\n\ndort zu schreiben z.B\n\n/*DA_INFO\nintervall=A\nDA_INFO*/\n\n/*BETREFF\naw12364, Ticket-568505, Datenauswertung zum Kartenverbund\nBETREFF*/\n\n/*IMPORT\nabteilung=ORG-EDV-DM\ndatei=einmalig_VC\ntabelle=TEMP.einmalig_VC\nparam=drop\nIMPORT*/ \n \n/*MAILTEXT\nHallo\nMAILTEXT*/\n \n/*XLS_EXPORT\ntabelle=TEMP.aw12364_1\ndatei=aw12364_1\nempf=S0802409 oder Ornder ohne per mail\nper_mail=true\nXLS_EXPORT*/\n\n4. In excel ein Datei mit irgendwelche Info aber <b>mit NAME - einmalig_VC</b> zu erstellen \nund speichern in Da_import_ORG_EDV_DM\n\n\n5.in sql schreiben, um status zu überprufen\n\nselect *\nvon s080idv.basis_dauerauftraege\nwhere letzte_ausf::date = current_date\n--where sql_name = 'DA_einmalig_VC'\n\n6. \n\nda_system\nmails - datei hier\nlogs - um zu prüfen `,
        "Antworten_Entwurf": ` \nich habe Ihnen die Tabellen per Mail gesendet. Bitte geben Sie mir eine Rückmeldung, ob Dateien plausibel sind und das Ticket geschlossen werden kann.\n\nMit freundlichen Grüßen\nVasily Chabanov`,
        "Neue Auftrag_Schritten": `Bearbeitung eines Tickets wie folgt beginnen:\n\n\n1.	In Wiki neue Auftragsnummer anlegen, dazu schauen, welche die letzte Auftragsnummer ist, entsprechend die nächst höhere Nummer wählen; dann im Feld „Auftragsnummer“ in folgender Forma angeben: aw12345, Ticket-987654, Ticketbetreff und im Feld „Ticket-URL“ die URL aus dem Ticket-System einfügen, dann „Seite anlegen“ drücken\n\n2.	Im Ticket eine „Interne Notiz erstellen“: in Titel und Text die neue „aw12345“ hinterlegen und den Status auf „in Arbeit“ setzen\n\n3.	Im SQL-Explorer eine neue Datei aw12345.sql anlegen\n\n4.	Select schreiben, gegebenenfalls SQL aus anderem Auftrag aus Wiki копировать; hierbei darauf achten, dass kein <SPAN…> im SQL steht; zwischen Statements dürfen keine Leerzeichen stehen\n\n5.	Versenden von Auswertungen immer über XLS_EXPORT; wenn an eine Person, dann Parameter per_Mail=true angeben, wenn Postkorb unter P:\\DA-Export\\ vorhanden, dann den Parameter nicht angeben\n\n6.Anpasungen in Code\n\n7.Code durchführen, um temp_tables zu erstellen\n\n8.File da_einmalig_VC File in da_select mit SQL zu öffnen\n\n8.alle /* Blöcken von aw12345 in da_einmalig_VC Paste\n\n9. Speichern Veränderungen in Sql\n\n10.Einmalig_Adhoc_Vasily von eihene Ordner in P/da-import-ordner von Abteilung Paste\n\n11.uberprüfen, ob zusätzliche File in da-select mit Name da_einmalig_VC_FEHLER nicht entsteht`,
        "Viele Werte in einer Feld": `SELECT unnest(\n	string_to_array(name_von_Spalte, E'\\n')\n	) AS werten\nFROM clients;\n`
    },
    Sys_admin: {
        "Meldung Bewegung": `1.SPKJ Ticket\n\n2. Ticket - Thema Meldung Bewegung Wirt...\n\n3.Anlagernummer aus Glpi\n\n4. Bezeichnung -LG Zoll 24 z.B.\n\n5. standorts aus pps Neo - Standortübersicht schreiben\n\n6.Grund - Austausch\n\n7.Nils`
    },
    update: {
        "Пример": `UPDATE table_name\nSET column1 = value1\nWHERE condition;`
    },
    delete: {
        "Пример": `DELETE FROM table_name\nWHERE condition;`
    },
    wortschatz: {
        "Основные слова": `Таблица – Tabelle – Table\nКолонка – Spalte – Column\nСтрока – Zeile – Row\nПервичный ключ – Primärschlüssel – Primary Key\nВнешний ключ – Fremdschlüssel – Foreign Key\nИндекс – Index – Index\nЗапрос – Abfrage – Query\nВыборка – Auswahl – Selection\nУсловие – Bedingung – Condition\nСоединение – Verbindung – Join\nСортировка – Sortierung – Order By\nГруппировка – Gruppierung – Group By\nАгрегатная функция – Aggregatfunktion – Aggregate Function\nСумма – Summe – Sum\nСреднее – Durchschnitt – Avg\nМаксимум – Maximum – Max\nМинимум – Minimum – Min\nПодзапрос – Unterabfrage – Subquery\nОбновление – Aktualisierung – Update\nУдаление – Löschen – Delete\nСоздание – Erstellung – Create\nВставка – Einfügen – Insert\nОграничение – Einschränkung – Constraint\nТриггер – Trigger – Trigger\nПросмотр – Ansicht – View\nИндивидуальный запрос – Individuelle Abfrage – Custom Query`
    },
    create: {
        "Пример": `CREATE TABLE table_name (\n    column1 datatype,\n    column2 datatype\n);`
    }
};
</script>
"""

# Zielordner: 'docs' im aktuellen Verzeichnis erstellen
output_root = "docs"
os.makedirs(output_root, exist_ok=True)

# Regulärer Ausdruck, um die Hauptkategorien zu finden
category_blocks = re.findall(r"(\w+):\s*\{([\s\S]*?)\},?\s*(?=\s*\w+:\s*\{|\s*\}\s*;)", html_content)

for cat_name, cat_content in category_blocks:
    # Verzeichnis für die Kategorie erstellen (z.B. docs/select, docs/DA_SPK)
    cat_dir = os.path.join(output_root, cat_name.lower())
    os.makedirs(cat_dir, exist_ok=True)
    
    # Die einzelnen Themen innerhalb der Kategorie parsen
    articles = re.findall(r'"([^"]+)":\s*`([\s\S]*?)`', cat_content)
    
    for title, text in articles:
        # Dateiname säubern (Leerzeichen durch Unterstriche ersetzen, Kleinbuchstaben)
        safe_title = title.replace(" ", "_").replace("/", "_").lower()
        file_path = os.path.join(cat_dir, f"{safe_title}.md")
        
        # HTML-Tags wie <b> und </b> durch Markdown ersetzen
        clean_text = text.replace("<b>", "**").replace("</b>", "**")
        
        # Inhalt für das Markdown-File vorbereiten
        md_content = f"# {title}\n\n"
        
        # Falls es sich um Code handelt (z.B. enthält SELECT, UPDATE, etc.), in einen Code-Block packen
        if "SELECT" in clean_text or "UPDATE" in clean_text or "DELETE" in clean_text or "CREATE" in clean_text or "drop table" in clean_text:
            # Wenn es reiner Code ist, formatieren wir es schön als SQL-Block
            if len(clean_text.strip().split('\n')) <= 3 or "Beispiel" in clean_text or "Anleitung" in title:
                md_content += clean_text.strip()
            else:
                md_content += f"```sql\n{clean_text.strip()}\n```"
        else:
            md_content += clean_text.strip()
            
        # Datei schreiben
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        print(f"Erstellt: {file_path}")

print("\n🎉 Fertig! Alle Dateien wurden erfolgreich in den Ordner 'docs/' exportiert.")