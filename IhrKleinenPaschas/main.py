from RealtimeSTT import AudioToTextRecorder
import pyautogui
import anthropic
import os
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("CLAUDE_KEY")
)

def fact_check(text):
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=20000,
        temperature=1,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Du hast die Aufgabe, ein Gespräch auf Fakten zu überprüfen. Du erhältst einzelne Sätze eins Transkriptes des Gesprächs und sollst jeden Satz auf faktische Fehler analysieren. So gehst du vor:\n\n1. Zuerst erhältst du das Gesprächstranskript:\n\n<conversation_transcript>\n" + text + "\n</conversation_transcript>\n\n2. Deine Aufgabe ist es, jeden Satz im Gespräch sorgfältig zu untersuchen und faktische Fehler zu identifizieren. Ein faktischer Fehler ist eine Aussage, die etablierten Fakten, wissenschaftlichen Erkenntnissen oder verifizierbaren Informationen widerspricht.\n\n3. Analysiere jeden Satz einzeln. Gehe nicht davon aus, dass Informationen aus einem Satz auf die faktische Richtigkeit eines anderen Satzes anwendbar sind oder diese beeinflussen, es sei denn, dies wird ausdrücklich angegeben.\n\n4. Bei der Identifizierung faktischer Fehler berücksichtige folgende Punkte:\n   - Historische Ungenauigkeiten\n   - Wissenschaftliche Fehlinformationen\n   - Falsche Statistiken oder Daten\n   - Falsche Behauptungen über Ereignisse, Personen oder Orte\n   - Fehldarstellung etablierter Fakten\n\n5. Für jeden Satz, der einen faktischen Fehler enthält, solltest du:\n   a) Den Satz zitieren\n   b) Erklären, warum er faktisch falsch ist\n   c) Die korrekte Information bereitstellen, falls möglich\n\n6. Präsentiere deine Ergebnisse in folgendem Format:\n\n<fact_check>\n<error_1>\n<quote>Füge den fehlerhaften Satz hier ein</quote>\n<explanation>Erkläre, warum dies faktisch falsch ist</explanation>\n<correction>Stelle die korrekte Information bereit, falls verfügbar</correction>\n</error_1>\n\n<error_2>\n<quote>Füge den nächsten fehlerhaften Satz hier ein</quote>\n<explanation>Erkläre, warum dies faktisch falsch ist</explanation>\n<correction>Stelle die korrekte Information bereit, falls verfügbar</correction>\n</error_2>\n\n(Setze dieses Muster für alle identifizierten Fehler fort)\n</fact_check>\n\nWenn keine faktischen Fehler im gesamten Gespräch gefunden werden, antworte mit:\n\n<fact_check>\nEs wurden keine faktischen Fehler in diesem Gespräch identifiziert.\n</fact_check>\n\nDenke daran, deine Rolle besteht nur darin, faktische Fehler zu identifizieren. Kommentiere nicht Grammatik, Meinungen oder subjektive Aussagen. Konzentriere dich ausschließlich auf verifizierbare Fakten."
                }
            ]
        }
    ]
    )
    for content_block in message.content:
        if content_block.type == "text":
            print(message.content)
    with open("C:\\Users\\aaron\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder5\\VSC\\IhrKleinenPaschas\\transcript.txt", "a") as file:
        file.write(text + "\n")
        file.write(format(message.content) + "\n")

if __name__ == '__main__':
    recorder = AudioToTextRecorder()

    while True:
        recorder.text(fact_check)