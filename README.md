# TFDownloader
Túlélők Földje nyilvános forduló letöltő csodacucc

nyilvDL.py

A "karik" listába be kell tenni vesszővel elválasztva azoknak a karaktereknek a számait akiknek a nyilvános fordulóit le akarjuk tölteni, aztán már mehet is a móka. Hardcore arcok betolhatják egyszerre az összes karaktert is, de akkor számolni kell vele, hogy kurva sokáig fog futni a script. 8000 fordulót kábé 26 perc alatt tölt le, jelenleg (2018. december 11.) nagyjából 120 ezer nyilvános forduló van, szóval ha minden karaktert egyszerre töltünk le, akkor a script kb. 6 és fél órán át fog dolgozni. Szóval érdemes talán apránként haladni. :-) Meg kell tárhely is! Mittomén kb. 20 giga, ha le akarjuk húzni mind a 100 ezer fordulót.

nyilvDL-inc.py

Ez meg úgy működik, hogy szintén a "karik" listába betesszük azoknak a karaktereknek a számait, akikre kiváncsiak vagyunk. Majd a "mikortol" változóba beírunk egy a mai napnál korábbi dátumot. Ezután mehet a móka és a script letölti a megadott karaktereknek a megadott dátum és a mai nap között keletkezett nyilvános fordulóit.
