# Grafika Komputerowa

Zbiór zadań laboratoryjnych z kursu Grafika Komputerowa realizowany w Pythonie.

## Struktura projektu

- **lab1/** – Rysowanie linii i okręgów, podstawy rasteryzacji.
- **lab2/**, **lab2b/** – Wprowadzenie do OpenGL, proste siatki 3D i oświetlenie.
- **lab3/** – Modele 3D i transformacje (skalowanie, obrót, translacja).
- **lab4/** – Interfejs użytkownika: przyciski, zdarzenia myszy oraz GUI z PyGame.
- **lab5/** – Ładowanie i wyświetlanie zewnętrznych modeli (np. czajnik Teapot) oraz zaawansowane ustawienia kamery.
- **lab6/** – Siatki 3D, GRID i wizualizacja wektorów.
- **lab7/** – Architektura komponentów (ECS), wyświetlanie normalnych i zaawansowane funkcjonalności.

## Wymagania

- Python 3.8 lub wyższy
- PyOpenGL
- PyGame

Zalecane utworzenie wirtualnego środowiska i instalacja zależności:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install PyOpenGL PyOpenGL_accelerate pygame
```

## Uruchamianie

Przykład uruchomienia programu z laboratorium 1:

```bash
python3 lab1/hellowindow.py
```

Przykład uruchomienia programu z laboratorium 4:

```bash
python3 lab4/AddingButton.py
```

Przykład uruchomienia programu z laboratorium 5:

```bash
python3 lab5/DisplayTeapot.py
```

Przykład uruchomienia programu z laboratorium 6:

```bash
python3 lab6/Grid.py
```

Przykład uruchomienia programu z laboratorium 7:

```bash
python3 lab7/Animate.py
```

## Licencja

Projekt udostępniony na licencji MIT.
