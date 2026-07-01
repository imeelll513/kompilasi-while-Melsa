# Simulasi Kompilasi Konstruksi If-Then-Else

> Tugas Akhir Mata Kuliah Teknik Kompilasi - Representasi 4 Tahap Kompilasi

---

## Pilihan Konstruksi

**Konstruksi yang dipilih:** Percabangan / Kondisi (If-Then-Else)

---

## Pattern (Pola Sintaks) - BNF Grammar

Pola didefinisikan menggunakan pendekatan **Backus-Naur Form (BNF)** sederhana:

```bnf
<if_stmt>      ::= "if" "(" <condition> ")" "{" <statements> "}" "else" "{" <statements> "}"

<condition>    ::= <identifier> <operator> <value>

<statements>   ::= <identifier> "=" <value>
