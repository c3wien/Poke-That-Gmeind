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
wir danken Ihnen herzlich, dass Sie sich für Luftfilter in Schulen und anderen öffentlichen Gebäuden und Einrichtungen stark gemacht haben. Wir würden uns sehr freuen, wenn Sie mithelfen, dass möglichst viele Menschen von luftfilterbegehren.at erfahren. Wir alle sind von der Covid-19 Pandemie und anderen aerosol-übertragenen Infektionskrankheiten betroffen und gemeinsam können wir etwas für unser aller Gesundheit tun.

1))) Senden Sie eine E-Mail an fünf Freund:innen. Hier ist ein Textvorschlag dafür:
"
Hallo,
ich habe gerade meine Gemeinde kontaktiert, um mich für Luftfilter in Schulen und anderen öffentlichen Gebäuden und Einrichtungen einzusetzen. Luftfilter anzuschaffen und zu installieren ist eine Möglichkeit, wie wir lokal und regional weitere Covid-19 Wellen verringern können.
Bitte schau dir www.luftfilterbegehren.at an und werde selbst für dich und dein Umfeld aktiv.
Hilf mit, unsere Gemeinde vorzubereiten!
Liebe Grüße,
"

2))) Sollte Ihnen Ihre Gemeinde geantwortet haben, haben wir für Sie unter https://luftfilterbegehren.at/konversationsleitfaden/ einen hilfreichen Gesprächsleitfaden mit Tipps und weiteren Informationen zusammengetragen.

3))) Gehen Sie den nächsten Schritt: Bleiben Sie mit Ihrer Gemeinde in Kontakt!
Die effektivste Art, Politiker:innen ins Gewissen zu reden ist, direkt mit ihnen zu sprechen. Rufen Sie in den nächsten Tagen auf Ihrem Gemeindeamt an, oder besuchen Sie die nächste Gemeinderatssitzung. Erinnern Sie Ihre Vertreter:innen daran -- die nächste Grippesaison kommt bestimmt.

Schöne Grüße,
Ihr Team von luftfilterbegehren.at
"""


MAIL_VALIDATE = """
Hallo {name_user},
vielen Dank für Ihren Einsatz für Luftfilter in Schulen und anderen öffentlichen Gebäuden und Einrichtungen! Damit Ihre E-Mail über www.luftfilterbegehren.at jetzt abgeschickt werden kann, müssen Sie die Übermittlung Ihres Namens ({name_user}) und Ihrer E-Mail-Adresse ({mail_user}) an die Gemeinde {name_city} bestätigen. Folgen Sie dazu diesem Link:
{url}

Mehr Informationen zur Verarbeitung Ihrer Daten erhalten Sie auf https://luftfilterbegehren.at/datenschutz/

Falls Sie nicht wissen, wieso Sie diese Nachricht erhalten haben oder mit der Übermittlung Ihrer Daten nicht einverstanden sind, ignorieren Sie diese Nachricht bitte.

Schöne Grüße,
das Team von luftfilterbegehren.at
"""
