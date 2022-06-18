#-*- coding: utf-8 -*-

MAIL_DISCLAIMER = "Diese E-Mail wird übermittelt im Namen von: {name_user}, {mail_user}"

MAIL_CITY = """
Liebe Gemeinde {name_city},
auch wenn viele Maßnahmen erlassen worden sind, ist die Gefahr durch die Covid-19 Pandemie noch nicht vorüber. Neben den Maßnahmen, die die Bundes- und Landesregierungen ergreifen und vorschreiben können, können aber auch Gemeinden etwas zum Schutz vor dieser und anderen Infektionskrankheiten ergreifen. Spezifisch möchte ich die Anschaffung und Installation von Luftqualitätsüberwachung und Lüftungs- bzw. Luftreinigungsgeräten für Schulen, Kindergärten und andere Gemeinderäumlichkeiten (Veranstaltungräume etc.) anregen.

Diese Empfehlung basiert auf dem Ende April 2022 veröffentlichten Arbeitspapier (Version 1.0, [1]) der Forschungsplattform Covid-19 Future Operations. Darin fordern die Mitglieder der Plattform Vorbereitungen für eine mögliche Corona-Welle im Herbst. Unter anderem empfehlen sie unter Punkt 3.3., "Technische/bauliche Adaptierungen" eben die Anschaffung und Installation von Luftqualitätsüberwachung und Lüftungs- bzw. Luftreinigungsgeräten. Weitere Details finden sich bereits im Jänner 2022 in einer Liste an Empfehlungen für den Infektionsschutz in Schulen (Version 1.1, [2]).

Die Effektivität von Luftreinigungsmaßnahmen wurde bereits in der italienischen Region Marche in einer Vergleichsstudie belegt: in Bildungseinrichtungen (Kindergarten bis Mittelschulen), die mit Lüftungstechnologie ausgerüstet waren, lag die Infektionsrate etwa 80% niedriger als in Einrichtungen ohne solche Ausrüstung ([3]). Auch in Österreich haben einzelne Städte und Gemeinden bereits Luftfilteranlagen u.a. in Schulgebäuden installiert -- es gibt also auch hierzulande bereits Erfahrungswerte, auf die zurück gegriffen werden kann ([4]).


Mit freundlichen Grüßen,
{name_user}

[1]: https://futureoperations.at/fileadmin/user_upload/k_future_operations/FUOP_Szenarien_Herbst-Winter_2022_Version_1.0.pdf
[2]: https://futureoperations.at/fileadmin/user_upload/k_future_operations/FOP_GrundregelnSchule_2022_06_01.pdf
[3]: https://www.fondazionehume.it/data-analysis/controlled-mechanical-ventilation-cmv-works/
[4]: https://traiskirchen.gv.at/news/virusbekaempfungs-luftreinigungsanlagen-in-allen-bildungseinrichtungen-traiskirchens/
"""

MAIL_WELCOME = """
Hallo {name_user},
wir danken dir herzlich, dass du dich für Luftfilter in Schulen und anderen öffentlichen Gebäuden und Einrichtungen stark gemacht hast. 

Wir würden uns sehr freuen, wenn du dabei mithilfst, dass möglichst viele Menschen von luftfilterbegehren.at erfahren. Wir alle sind von der Covid-19 Pandemie und anderen aerosol-übertragenen Infektionskrankheiten betroffen und gemeinsam können wir etwas für unser aller Gesundheit tun.

1))) Sende eine E-Mail an fünf Freund*innen. Hier ist ein Textvorschlag dafür:
"
Hallo,
ich habe gerade meine Gemeinde kontaktiert, um mich für Luftfilter in Schulen und anderen öffentlichen Gebäuden und Einrichtungen einzusetzen. Luftfilter anzuschaffen und zu installieren ist eine Möglichkeit, wie wir lokal und regional weitere Covid-19 Wellen brechen können.

Bitte schau dir https://luftfilterbegehren.at an und werde selbst für dich und dein Umfeld aktiv!

Liebe Grüße,
"

2))) Sollte dir deine Gemeinde antworten, findest du unter https://luftfilterbegehren.at/konversationsleitfaden/ Tipps und weitere Informationen für einen konstruktiven Austausch und weiteres Vorgehen.

3))) Geh' den nächsten Schritt: Bleib' mit deiner Gemeinde in Kontakt!
Die effektivste Art, Politiker*innen ins Gewissen zu reden ist, direkt mit ihnen zu sprechen. Ruf in den nächsten Tagen auf deinem Gemeindeamt an, oder besuch die nächste Gemeinderatssitzung. Erinnere deine Vertreter*innen daran: die nächste Grippesaison kommt bestimmt.

Schöne Grüße,
das Team von luftfilterbegehren.at
"""


MAIL_VALIDATE = """
Hallo {name_user},
vielen Dank für deinen Einsatz für Luftfilter in Schulen und anderen öffentlichen Gebäuden und Einrichtungen! Damit deine E-Mail über www.luftfilterbegehren.at jetzt abgeschickt werden kann, musst du die Übermittlung deines Namens ({name_user}) und deiner E-Mail-Adresse ({mail_user}) an die Gemeinde {name_city} bestätigen. Folge dazu diesem Link:
{url}

Mehr Informationen zur Verarbeitung deiner Daten findest du auf https://luftfilterbegehren.at/datenschutz/

Falls du nicht weißt, wieso du diese Nachricht erhälst oder mit der Übermittlung deiner Daten nicht einverstanden bist, ignoriere diese Nachricht bitte einfach.

Schöne Grüße,
das Team von luftfilterbegehren.at
"""
