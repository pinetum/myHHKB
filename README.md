myHHKB
==================================

Sparkfun Pro Micro (Arduino leonardo) + TMK firmware + HHKB

### Features

- Use Arduino [bootloader](https://github.com/sparkfun/SF32u4_boards/blob/master/sparkfun/avr/bootloaders/caterina/Caterina.c)

### Requirement

- install make
- Install Arduino
- Add avr-gcc to PATH `/Applications/Arduino.app/Contents/Java/hardware/tools/avr/bin/`
- clone git submodule

#### Downloading

```bash
cd keyboard/hhkb
make claean
# compile for keymap_????.c
make KEYMAP=????  
# let pro micro enter bootloader mode
# download
python downloader.py
```

[For first time use, you can enter bootloader mode by pulling the RST pin low.](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide/troubleshooting-and-faq#ts-reset)

### HHKB connector lines:

|JP  | Pro2 |  Pro  |   Function  |  Description                           |    TMK pin usage|Sparkfun Pro micro pin|
|----|-------|-------|-------------|--------------------------------------|-----------------------|---|
|     |      |      1 |     Vcc(5V)|                                       |        5V|VCC|
|     1  |  1   |   2     | Vcc(5V)       |                            |            5V|VCC|
|     2 |   2   |   3    |  Vcc(5V)   |                                         |   5V|VCC|
|     3 |   3   |   4     | TP1684    |  ~KEY: Low(0) when key is pressed       |   PD7 input(with pullup)|6|
|     4 |   4   |   5    |  TP1684     | HYS: High(1) when key is pressed        |  PB7 output|7|
|     5 |   5   |   6    |  HC4051     | A(bit0)\                                |  PB0 output|A2|
|     6 |   6   |   7     | HC4051     | B(bit1) > select row 0-7                |  PB1 output|A1|
|     7 |   7   |   8     | HC4051     | C(bit2)/                                |  PB2 output|A0|
|     8 |   8   |   9     | LS145       |A(bit0)\                                |  PB3 output|14|
|     9 |   9   |  10     | LS145      | B(bit1) > select column 0-7             |  PB4 output|8|
|    10 |  10   |  11     | LS145      | C(bit2)/                                |  PB5 output|9|
|    11 |  11   |  12     | LS145      | ~D(enable) Low(0) enables selected column |PB6 output|10|
|    12  | 12  |   13     | GND         |                                         | GND|GND|
|    13  | 13  |   14     | GND         |                                         | GND|GND|
|       |     |   15    |  GND|||
|    14  |      |        |  HC4051(Z2) | ~Enable of Z2   row0-7                  |  PC6|X|
|    15  |      |         | HC4051(Z3) | ~Enable of Z3   row8-15                 |  PC7|X|