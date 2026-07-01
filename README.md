# Simulasi Kompilasi Konstruksi While Loop

> Tugas Akhir Mata Kuliah Teknik Kompilasi - Representasi 4 Tahap Kompilasi

---

## Deskripsi Proyek

Proyek ini adalah simulasi sederhana dari proses kompilasi untuk konstruksi **perulangan while** dalam bahasa pemrograman. Program ini mendemonstrasikan bagaimana sebuah source code diproses melalui 4 tahapan utama kompilasi:

1. **Lexical Analysis** (Analisis Leksikal)
2. **Syntax Analysis** (Analisis Sintaks)
3. **Semantic Analysis** (Analisis Semantik)
4. **Three-Address Code Generation** (Generasi Kode Tiga Alamat)

---

## Tujuan

- Memahami alur kerja compiler dari source code hingga kode antara (TAC)
- Mengimplementasikan konsep BNF Grammar dalam parsing
- Membangun Abstract Syntax Tree (AST) dari source code
- Menghasilkan Three-Address Code yang siap untuk optimasi dan code generation

---

## BNF Grammar

Program ini mendukung source code dengan format:

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