# 🤖💡 LangOllamaQ(深蓝)

<div align="center">

[简体中文](README_CN.md) / [繁体中文](README_TC.md) / [English](README.md) / Deutsch / [日本語](README_JP.md)

</div>

---

## 🌐 <span style="color: #2ecc71;">Zusammenfassung des projekts</span>

 🤖Der name langoladq ist ein ortsweites abgrundsystem mit moderner technik. Darauf gründet es <span style="color: #e74c3c;">LangChain</span> und 📚 <span style="color: #e74c3c;">Rama ist ein bauprojekt</span> Sie bauten.Sie ist in der Lage, mehrere dokumente aus lokalen ordnern so einfach wie möglich zu laden, dass sie einbetten und speichern in die vektordatenbank, fragen im kontext des dokuments eingeben, den verlauf der dialoge dokumentieren und eine fortlaufend interaktion verknüpfte abgleichbare assistent der ad hoc -semantischen suche erstellen.🔍📚

###  <span style="color: #f1c40f;">Eindruck machen.</span>

- ** dokument-unterstützung ** : recode-ordner durchsuchen, wird alle pdf-dokumente geladen 📁
- ** effektive vektoren speichern ** : mit dem ollatans modell die textinfos aufbauen und speichern. ** effektive recherchen unterstützen. 🔍
- ** semantische fragen ** : "in der verknüpfung erhalten perfekte und dem kontext angepasste antworten." 💬
- ** gedächtnismodul ** : aufzeichnungen der benutzerkennung zur person erfassen und dynamische abfrage, aktualisierung und säuberung unterstützen. 💾
- ** erweiterte dokumentation ** leichter einbindung anderer dokumenttypen (wie z. B. TXT, nachxt) Oder verlängerte vektoren 🔧

> 💡 <span style="color: #f1c40f;"> And * pass auf! Das produkt befindet sich derzeit in der testphase und stellt eine riesige menge zur verfügung, die lediglich für die tests zur verfügung steht. Wenn ein produkt in der realen umgebung eingesetzt wird, müssen die nutzer bei bedarf die besonderen kenntnisse des sektors berücksichtigen.

### <span style="color: #9b59b6;">Die struktur des projekts</span>

```plaintext
LangOllamaQ/
├── documents/
│   # Alle pdf-dokumente speichern
├── loader/
│   └── pdf_loader.py
│       # Durchsuchen und laden sie die dokumente aus den ordnern
├── embeddings/
│   └── generate_embeddings.py
│       # Zum erzeugen Von vektoren eingebettet und gespeichert
├── qa/
│   └── qa_with_context.py
│       # Gibt antworten aus dem kontext
├── memory/
│   └── memory_manager.py
│       # Aufzeichnungen und aufzeichnungen der benutzer-dialoge zu führen
├── main.py
│   # Der haupteingang.
├── requirements.txt
│   # Dateien betrachten
├── .gitignore
│   # Dateien ignorieren
└── README.md
    # Dokumentationen über das projekt.
```
###  <span style="color: #e67e22;">Schnell zugreifen.</span>

#### Ein projekt des klonens 🖥️
```bash
git clone https://github.com/abossss/LangOllamaQ.git
cd LangOllamaQ
```
### Eine abhängigkeit danach 📦
Empfiehlt den einsatz des virtuellen umweltmanagements für abhängigkeit：

#### Virtuelle umgebung schaffen
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```
## Eine abhängigkeit danach.

```bash
pip install -r requirements.txt
```

## Dokumente hinzufügen 📄
Und pdf-dateien hinzufügen ` documents / ` ordner.

## Leite sequenz an. 🚀
```bash
python main.py
```

Verfahren automatisch geladen ` documents / ` - alle pdf-dateien, die vector eingebettet, und interaktiven: modell.

##  <span style="color: #1abc9c;">Spezieller befehl.</span>
- aus: geben ` q ` 🚪
-  : geben ` clear ` 🧼

##  <span style="color: #3498db;">Gestaltung des baumes</span>

### Füll das modul ab (loader/pdf_loader.py)
```
Bereithalten zum einlesen des angegebenen ordners und laden alle pdf-dokumente nach Seitenweise wird die riesendatei geladen.
Funktion kernfunktion：`load_documents_from_folder(folder_path)`
```
### Moduls einbetten (embeddings/generate_embeddings.py)
```
Er erstellt die anzeige des vektors mit dem prüfmodell Von olpa und wird als speichervektordatenbank mähmt.
Funktion kernfunktion：`generate_embeddings(docs)`
```
### Frage für modul. (qa/qa_with_context.py)
```
Recherchen zum aktuellen kontext der benutzerfragen, um antworten aus der vektordatenbank zu erhalten
```
### Speichermodul einrichten.（memory/memory_manager.py）
```
Erfassen sie fragen und antworten des benutzers, unterstützen sie kontextabhängige kongruenzen und gedächtnislöschung
Die funktion kernfunktion:
add_to_memory(question, answer)
get_full_memory()
clear_memory()
```

## 🌟 Maestro. Wie sind sie

## Lädt das dokument und gibt die antwort heraus
Nehmen wir an, sie hätten die folgenden fragen：
```
> Bitte fassen sie die fakten zusammen
```
Das programm holt aus dem ausgewählten dokument den kontext ab und gibt die folgenden antworten heraus：
```
> Dieser text behandelt vor allem die probleme bei der verarbeitung grafischer daten der grafischen netzwerke, vor allem die geometrischen verbesserungen der sichtbarkeit. Hier sind einige schlüsselfaktoren:

1. ** probleme in der trainings-phase. ** die grafischen netzwerke werden bei der übung mit gleichziehen (over smootorts) und squassis in verbindung gebracht. Die probleme ergeben sich aus der zunahme der netzwerktiefe, aufgrund derer die knoten die annahme haben, daß informationen Von belang Oder nicht identifizierbar sind.

2. ** um diese probleme mit hilfe Von rekonstruktion zu lösen, ** : eine abmilderung ist die anwendung Von presentative verfahren mit prohibitiven proportionen, der "wiederholung" -prozess. Mit dieser methode werden ränder in gebieten mit hohem krümmgrad entfernt und neue ränder in gebieten mit niedrigen krümmungswerten hinzugefügt, um die auswirkungen Von sanften und exzessiven belastungen zu verringern

3. ** verhaltene lernfähigkeit Von neuronalen netzwerken. ** das standard-nachrichtenübertragungs-system BNS kann nicht lernen, dass wenn die beiden bilder verschieden sind, verschiedene beziehungen setzen. Das bedeutet, dass es dem GNN möglicherweise nicht möglich ist, einige seiner grundlegendsten aufgaben wie die berechnung des graphikdurchmesser Oder die bestimmung des maximalen ringumfangs zu erlernen.

4. ** möglichkeiten zur erweiterung der sichtbar macht: kann es zusätzliche geometrische informationen geben, um die leistung der neuronalen netze zu verbessern, kann es etwa mit Laplacian spectrum und trum ausgedrückt werden. Diese technologien können bei GNNs mehr über die struktur der grafik lernen.

5. ** die auf diskrete krümmungsweise beruhende informationsverhaftung ** * : die diphoretischen krümmungen erfassen lokale nachrichten eines gebrochenen nachbarn, während die informationskanäle nur einen bezug zu einem nachbarn haben.

Dieser beitrag hat jedoch nahegeleitet, wie grafische neuronale netzwerke mittels geometrie die bestehenden grenzen überwinden und ihre kapazität zur grafischen datenverarbeitung verbessern können. Diese ansätze stellen einen effektiven weg dar, um das problem der GNS zu lösen und gleichzeitig die Von den knotenpunkte verursachten wissensprozesse zu verbessern, so dass sie sich besser auf anwendungen bei fließender arbeit einstellen.
```
## Die geschichte der dialoge
Die benutzer können den kontext bei den sich überschneidenden dialogen bewahren:
```
Sie was ist das herzgeschäft des Aurora arms?
深蓝: das herzstück des aury-teams ist die förderung der anwendung Von technologien der künstlichen intelligenz in bildung, medizin und industrie.
```
```
Sie: was ist ihr ziel?
深蓝: das team Von arg blue setzt sich dafür ein, eine neue generation Von talents zu entfachen und technologische innovation anzustoßen.
```
Nutzer geben ` clear ` :
```
sie：clear.
深蓝: die geschichte des dialogs ist gelöscht.
```
Nutzer geben ` q ` aus verfahren
```
Sie：q.
Das programm wurde gekündigt. Es funktioniert nicht
```
## 🛠️ Die technologieschändung

- Die programmiersprache：**Python >= 3.8**
- Modelle.：**Ollama Embeddings**, **Ollama LLM**
- Rahmen.：**LangChain**
- Datenbank: Speicher mit speichervektoren（Expandieren kann durch **Pinecone**、**Weaviate** auf）

## 📖 Expandieren.

- **Unterstützung anderer dokumentformat**：
  - Zurzeit nur unterstützt. **PDF**，Zukunft kann zur unterstützung ausgeweitet werden **.txt**、**.docx** In wievieltem format。
- **Der langfristige vektor wird gespeichert**：
  - Es wird die speichersspeilung verwendet und empfohlen, die erweiterung basiert **SQLite**、**Pinecone** Der transport Von dauer lagern.
- **Integrierten API**：
  - Sie können zugießen. **RESTful** Oder **gRPC** Interface，Und sie können einbindung in das vordere Oder andere system erleichtern
- **Cloud setzt sich in stellung**：
  - Zur verfügung **AWS**、**GCP** Oder **Azure** Gewebe zu funkturm erstellen
- **Unterstützung zum thema mehrsprachigkeit**：
  - Aktuelle voreinstellung lautet **Das ist chinesisch.**，Unterstützung in bezug auf mehrsprachige fragen。

## 🤝 Das ist eine anleitung.

Willkommen zum quellcode, zur meldung Von programmfehlern Oder zur vorlage Von funktionsbedürfnissen!

## 📜 Erlaubnis.

Dieses programm ist ein gpl-modul mit * logikk und k, und es ist ein offenes verwenden und änderungen willkommen.
