# Tipos de dados.

- no computador: bits
- sempre reunidos em grupos: byte (grupo de 8 bit), word...
- a CPU tem dois componentes que lidam com:
  - inteiros: a ULA (unidade lógica e aritmética)
  - floats: FPU (unidade de ponto flutuante)
- no sistema operacional: bytes e arquivos
- na linguagem: strings, ints, floats, booleans, listas,...

## Arquivos

- arquivos são meros depósitos de bytes (bits, em última
  instância)
- use o comando `xxd -b <arquivo>` para listar bits
- na prática, é inconveniente usarmos bits, por isso usamos
  hexadecimais
- use o comando `xxd <arquivo>` pra listar hexadecimais
- se o arquivo é ASCII, caracteres == bytes
- se o arquivo é UNICODE, precisa de codificação extra
- utf-8: forma de codificação mais convencional para UNICODE
  - pode ser visto como extensão de ASCII
  - para os caracteres que são ASCII, só usa um byte
  - para os caracteres que não são, usa vários bytes
  - exemplos:
    - `casa` cabe em 4 bytes
    - `josé` cabe em 5 bytes (o `é` precisa de 2)

> Confira no bash que o arquivo `exemplo.txt` tem 4 caracteres,
> mas codificados em um total de 7 bytes. Use `ls -l` pra ver a
> contagem de bytes do SO. Use `cat` pra imprimir o arquivo. Use
> `xxd exemplo.txt` para ver cada um dos bytes (em hexadecimal)
> que compõem o arquivo. Confira cada byte na tabela ASCII
> (busque-a na internet).


## camadas de abstração 

Quando programamos, atravessamos várias camadas de abstração.
Cada uma delas introduz seus próprios tipos de dados. É
importante ser capaz de entender e usar as abstrações, mas sem
deixar de entender que é apenas isso: uma abstração. Pra isso, é
preciso compreender bem como cada camada funciona. Isso ajuda a
resolver problemas que surgem.

Estas são as camadas que nos distanciam da máquina.

1. nossos programas ou outros aplicativos
2. a linguagem (python, no nosso caso)
3. o sistema operacional
4. a máquina

## Tipos de dados em Python

- `int`: representa inteiros
  - representa valores inteiros (positivos e negativos)
  - é de tamanho arbitrário (diferente de outras linguagens)
  - o limite é apenas o espaço de memória disponível
- `float`: representa números com ponto decimal
  - embora nos lembre dos reais, não são números reais
  - são uma mera codificação de ponto decimal sobre bits
  - incluem um erro inerente à representação (0.1 + 0.1 + 0.1)
- `str`: representa dados textuais
  - em Python, caracteres e bytes são diferentes
  - em outras linguagens, os conceitos se confundem
  - caracteres são elementos de UNICODE
  - excelente para representar strings na memória principal
- `bytes`: representa strings de _bytes_
  - sequências de bytes (8 bits) puros
  - tipo e literal próprios: `b"abc"` (o `b` indica bytes)
  - excelente para interagir com o mundo externo ao processo
    - arquivos no SO, por exemplo, são apenas bytes
    - conexões internet, idem
    - outros dispositivos, idem
