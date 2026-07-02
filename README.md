
# Simulasi Kompilasi Konstruksi While Loop

> Tugas Akhir Mata Kuliah Teknik Kompilasi - Representasi 4 Tahap Kompilasi

---

## Pilihan Konstruksi

**Konstruksi yang dipilih:** Perulangan (Looping) - **While Loop**

---

## Pattern (Pola Sintaks) - BNF Grammar

Pola didefinisikan menggunakan pendekatan **Backus-Naur Form (BNF)** sederhana:

```bnf
<program>      ::= <while_stmt>

<while_stmt>   ::= "while" "(" <condition> ")" "{" <statement> "}"

<condition>    ::= <identifier> <rel_op> <number>

<statement>    ::= <assignment>

<assignment>   ::= <identifier> "=" <expression> ";"

<expression>   ::= <identifier> "+" <number>
                 | <identifier> "-" <number>
                 | <number>
                 | <identifier>

<rel_op>       ::= "<" | ">" | "<=" | ">=" | "==" | "!="

<identifier>   ::= letter (letter | digit)*

<number>       ::= digit+
