# Live lecture transcription

`transcribe_lecture_live.py` trascrive l'audio riprodotto su Linux con PulseAudio
o PipeWire tramite `pipewire-pulse`. Lo script è autonomo: non richiede
`transcribe_lecture.py` nella stessa cartella. Richiede le librerie Python
`faster-whisper`, `huggingface-hub`, `tqdm` e `numpy`, oltre a `ffmpeg` con supporto
PulseAudio e `pactl`. La cartella opzionale `.transcribe-cuda` viene cercata accanto
allo script e nella cartella superiore.

## Avvio

Metti il video in pausa, avvia lo script e riprendi quando compare `Capture active`:

```bash
python3 transcribe_lecture_live.py -o lezione-live.txt
```

Il modello predefinito è `base.en`, per lezioni in inglese. Il primo avvio può
richiedere il download del modello. Per italiano usa un modello multilingue:

```bash
python3 transcribe_lecture_live.py --model small --language it -o lezione-italiano.txt
```

Per usare il modello inglese più accurato dello script originale:

```bash
python3 transcribe_lecture_live.py --model medium.en --device cuda -o lezione-live.txt
```

Il testo appare nel terminale e viene salvato dopo ogni segmento. `Ctrl+C` ferma
la cattura e completa la trascrizione dell'audio già acquisito. Un secondo
`Ctrl+C` interrompe subito e scarta l'audio ancora da elaborare.
I file esistenti non vengono sovrascritti.

## Sorgente audio

Lo script sceglie il monitor dell'uscita audio predefinita all'avvio. Cattura
tutti i suoni di quell'uscita, incluse notifiche e altre applicazioni.
Il microfono non viene selezionato automaticamente.
Per scegliere un'altra uscita, ad esempio cuffie:

```bash
python3 transcribe_lecture_live.py --list-sources
python3 transcribe_lecture_live.py --source NOME_USCITA.monitor -o lezione-live.txt
```

Se cambi uscita durante la sessione, riavvia lo script con la nuova sorgente
e un nuovo file di destinazione.

## Latenza e limiti

- Il testo arriva per blocchi di 8 secondi, più il tempo di calcolo. Riduci
  `--chunk-seconds`, per esempio a `4`, per aggiornamenti più frequenti.
- I blocchi sono indipendenti e non sovrapposti: parole o frasi al confine
  possono perdere accuratezza. Non sono sottotitoli istantanei parola per parola.
- Se il modello è più lento del video, lo script conserva l'audio su disco e
  segnala il ritardo. Prova `--model tiny.en` oppure `--device cuda`.
- Il buffer temporaneo usa circa 115 MB per ora di cattura e viene eliminato
  all'uscita; non costituisce una registrazione permanente di backup.
- I timestamp partono dall'inizio della cattura, non dalla posizione del video.
  Pause, cambi di velocità e salti nel video non vengono rilevati.
- `--duration 60` limita la cattura a 60 secondi. `--plain` omette i timestamp.
- `--language auto` richiede un modello multilingue e rileva la lingua per blocco.

Riferimenti: [ingresso PulseAudio di FFmpeg](https://ffmpeg.org/ffmpeg-devices.html#pulse),
[faster-whisper](https://github.com/SYSTRAN/faster-whisper).
