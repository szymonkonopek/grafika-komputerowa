# 🎮 Interaktywny Rysownik Linii (Pygame)

To prosty projekt **Pygame**, który pozwala użytkownikom rysować linię **stopniowo** między dwoma punktami, wykorzystując **algorytm Bresenhama**. Początek i koniec linii można ustawiać interaktywnie za pomocą **myszy**.

## ✨ Funkcje

- **Stopniowe rysowanie linii**: Linia jest rysowana piksel po pikselu z widocznym efektem.
- **Interaktywne sterowanie**:
  - **Lewy przycisk myszy** 🖱️ → Ustaw **punkt początkowy** linii.
  - **Prawy przycisk myszy** 🖱️ → Ustaw **punkt końcowy** linii.
- **Pętla rysowania**: Po pełnym narysowaniu linii ekran jest czyszczony i proces rozpoczyna się od nowa.
- **Wykorzystuje tylko podstawowe funkcje rysowania pikseli** (bez wbudowanego `pygame.draw.line`).

---

## 📦 Instalacja

### 1️⃣ **Sklonuj repozytorium**

```sh
git clone https://github.com/szymonkonopek/interaktywny-rysyownik-lini.git
cd interaktywny-rysyownik-lini
```

### 2️⃣ Utwórz wirtualne środowisko (Opcjonalnie, ale zalecane)

```sh
python -m venv venv  # Tworzenie wirtualnego środowiska
```

- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 3️⃣ Zainstaluj biblioteki (Pygame)

```sh
pip install -r requirements.txt
```

## 🕹️ Użycie

### Uruchom program

```sh
python main.py
```

## 🔧 Jak to działa

- Projekt wykorzystuje algorytm Bresenhama, który efektywnie oblicza, które piksele należy wypełnić, aby utworzyć gładką linię między dwoma punktami. Zamiast natychmiastowego rysowania linii, pojawia się ona stopniowo, co czyni proces rysowania widocznym w czasie rzeczywistym.
