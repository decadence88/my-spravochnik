# Инструкция:`DA_einmalig_VC`

=== "Основная инструкция"

    ???+ excel "1. Создание таблицы в БД "
        ```sql
        drop table if exists TEMP.aw12364_1;
        create table TEMP.aw12364_1 as (SQL_CODE) with data;
        ```

    ??? excel "2. Выполнение кода "
        Code durchführen, um Tabellen zu erstellen

    ??? excel "3. Конфигурационный файл "
        `da_selects` mein Datei - `DA_einmalig_VC` dort zu schreiben z.B:
        ```text
        /*DA_INFO
        intervall=A
        DA_INFO*/

        /*BETREFF
        aw12364, Ticket-568505, Datenauswertung zum Kartenverbund
        BETREFF*/

        /*IMPORT
        abteilung=ORG-EDV-DM
        datei=VC_AW
        tabelle=TEMP.VC_AW
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

        ```

    ??? excel "4. Подготовка файла Excel "
        In excel ein Datei mit irgendwelche Info aber **mit NAME - einmalig_VC** zu erstellen und speichern in `Da_import_ORG_EDV_DM`

    ??? excel "5. Проверка статуса в SQL "
        In sql schreiben, um status zu überprüfen:
        ```sql
        select * von s080idv.basis_dauerauftraege
        where letzte_ausf::date = current_date
        --where sql_name = 'DA_einmalig_VC'
        ```

    ??? excel "6. Проверка системных логов "
        `da_systemmails` - datei hier `logs` - um zu prüfen
