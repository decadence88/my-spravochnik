# Export Tabelle zur Kollegen

```sql
1.
drop table if exists TEMP.aw12364_1;
create table TEMP.aw12364_1 as (
SQL_CODE SQL_CODE SQL_CODE SQL_CODE SQL_CODE
) with data;

2.Code durchführen, um Tabellen zu erstellen

3. da_selects
mein Datei - DA_einmalig_VC

dort zu schreiben z.B

/*DA_INFO
intervall=A
DA_INFO*/

/*BETREFF
aw12364, Ticket-568505, Datenauswertung zum Kartenverbund
BETREFF*/

/*IMPORT
abteilung=ORG-EDV-DM
datei=einmalig_VC
tabelle=TEMP.einmalig_VC
param=drop
IMPORT*/ 
 
/*MAILTEXT
Hallo
MAILTEXT*/
 
/*XLS_EXPORT
tabelle=TEMP.aw12364_1
datei=aw12364_1
empf=S0802409 oder Ornder ohne per mail
per_mail=true
XLS_EXPORT*/

4. In excel ein Datei mit irgendwelche Info
aber **mit NAME - einmalig_VC** zu erstellen 
und speichern in Da_import_ORG_EDV_DM


5.in sql schreiben, um status zu überprufen

select *
von s080idv.basis_dauerauftraege
where letzte_ausf::date = current_date
--where sql_name = 'DA_einmalig_VC'

6. 

da_system
mails - datei hier
logs - um zu prüfen
```