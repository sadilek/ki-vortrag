0\.

- KI ist in aller Munde. In den Medien wird viel diskutiert über wirtschaftliche und gesellschaftliche Implikationen.
- Darum soll es in diesem Vortrag im Wesentlichen nicht gehen.
- Stattdessen ist das Ziel: Neuronale Netze im Detail zu verstehen, so dass wir sie mit Stift/Papier ausführen könnten.
- Die Mathematik von neuronalen Netzen ist auf Schulniveau.
  - Es werden Zahlen miteinander multipliziert und aufaddiert.
  - Daneben nur: Ableitung/Steigung einer Funktion.
	
- Keine normalen Präsentationsfolien, stattdessen interaktive Programmierumgebung / Taschenrechner auf Steroiden.
- Hallo Welt.
- Vorstellung davon, wie KI-Entwickler und Datenwissenschaftler arbeiten.
	
1\.

- Bevor wir einsteigen, zunächst eine Einordnung.

1.2. Einordnung

- Dafür brauchen wir Konzepte, die es lohnend machen, dass wir uns auch regel-basierte und statistische KI anschauen.
- Maschinelles Lernen: Lernen aus Daten.
- Unüberwachtes Lernen: Rohdaten ohne "Beschriftung": Ziel ist, Struktur in den Daten zu finden.
- Überwachtes Lernen: Daten mit Beschriftung.

2.2.

- Bei KI geht es darum, eine Funktion zu implementieren.

2.3.

- Neuronale Netze rechnen mit Kommazahlen. Die Eingabe sind Zahlen und die Ausgabe sind Zahlen.
- Wir haben Einzelwerte, Listen, Tabellen, Quader, ...
- Verallgemeinert sind dies alles "Tensoren".

2.4.

- Daten: 70k Bilder von handgeschriebenen Ziffern.
- Aufgeteilt in 60k Trainingsbeispiele und 10k Testbeispiele.
- X: Eingabe, y: erwartete Ausgabe.
- Wie kann eine Ziffern-erkennende Funktion aussehen?
- Idee: Errechnung der durchschnittlichen Ziffer und Vergleich zu erkennender Ziffer damit.

3\.

- Unser Ziel ist nun, das MNIST Problem per neuronalem Netz mit höherer Genauigkeit zu lösen.
- Die Idee des ML ist es, die zu implementierende Funktion, nicht händisch zu programmieren, sondern
  - eine generische Funktion zu verwenden, deren Verhalten durch Änderung von Parametern gesteuert wird, und
  - die Parameter gemäß Beispieldaten anzupassen.
- Diese zwei Konzepte müssen wir zunächst verstehen, bevor wir ein neuronales Netz bauen können.

3.1.

- Hier kann man sich vorstellen, dass ein paar Punkte gegeben sind und man probiert, a, b und c so zu wählen, dass die Kurve möglichst dicht an den Punkten liegt.

3.2.

- Wir berechnen ein Fehlermaß (loss), dass uns sagt, wie gut der gewählte Parameterwert ist.
- Da wir nur ein Parameter haben, können wir hier das Fehlermaß für alle möglichen Parameter wählen.
- Im neuronalen Netz wird dies nicht mehr möglich sein! Zu viele Parameter.
- Deswegen brauchen wir eine Möglichkeit, die Parameterwerte mit dem geringsten loss zu finden, ohne den less für alle Parameterwerte zu berechnen.
- Genau das erlaubt uns das Gradientenverfahren.

3.3.

- Biologisch inspiriert.

3.5.

- Wir kehren jetzt zur Ziffernerkennung zurück.

4\.

- Die Aufgabe mit der GPT trainiert wird, ist für einen Textschnipsel das wahrscheinlichste nächste Wort vorherzusagen.
