# Neue Auftrag_Schritten

Bearbeitung eines Tickets wie folgt beginnen:


1.	In Wiki neue Auftragsnummer anlegen, dazu schauen, welche die letzte Auftragsnummer ist, entsprechend die nächst höhere Nummer wählen; dann im Feld „Auftragsnummer“ in folgender Forma angeben: aw12345, Ticket-987654, Ticketbetreff und im Feld „Ticket-URL“ die URL aus dem Ticket-System einfügen, dann „Seite anlegen“ drücken

2.	Im Ticket eine „Interne Notiz erstellen“: in Titel und Text die neue „aw12345“ hinterlegen und den Status auf „in Arbeit“ setzen

3.	Im SQL-Explorer eine neue Datei aw12345.sql anlegen

4.	Select schreiben, gegebenenfalls SQL aus anderem Auftrag aus Wiki копировать; hierbei darauf achten, dass kein <SPAN…> im SQL steht; zwischen Statements dürfen keine Leerzeichen stehen

5.	Versenden von Auswertungen immer über XLS_EXPORT; wenn an eine Person, dann Parameter per_Mail=true angeben, wenn Postkorb unter P:\DA-Export\ vorhanden, dann den Parameter nicht angeben

6.Anpasungen in Code

7.Code durchführen, um temp_tables zu erstellen

8.File da_einmalig_VC File in da_select mit SQL zu öffnen

8.alle /* Blöcken von aw12345 in da_einmalig_VC Paste

9. Speichern Veränderungen in Sql

10.Einmalig_Adhoc_Vasily von eihene Ordner in P/da-import-ordner von Abteilung Paste

11.uberprüfen, ob zusätzliche File in da-select mit Name da_einmalig_VC_FEHLER nicht entsteht