# GPT Voice Assistant

This is a voice assistant that utilizes the powerful GPT-3.5 language model. When you want to use it, just say 'Hola gpt' and ask it whatever you want.

## Installation

```bash
git clone https://github.com/pablodorrio/gpt-voice-assistant
```

## Set up

### Persistent use

For Linux and macOS users:

```bash
echo 'export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"' >> ~/.bash_profile

echo 'python3 THE_ROUTE_OF_THE_MAIN_FILE' >> ~/.bash_profile
```

For Windows users:
1. Press Windows + R, type taskschd.msc and press Enter.
2. Select create task.
3. In the "General" section, in the "Name" box, type "gpt-voice-assistant" and select the option "Run only when the user is logged in".
4. In the "Actions" section, press "New" and in the "Program or script" box type "python THE_ROUTE_OF_THE_MAIN_FILE" and press "Accept".
5. In the "Conditions" section uncheck all options and press "Accept".

### Test use

For Linux and macOS users:
```bash
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

For Windows users:
```powershell
$Env:OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

## Usage

### Persistent use

The assistant is launched each time you Log in so it will already be available for use.

### Test use

For Linux and macOS users:
```bash
python3 src/main.py
```

For Windows users:
```powershell
python .\src\main.py
```

### Once the programme has started:

Say "Hola gpt" to start the voice recognition and ask the questions you want.

Say "Adiós gpt" when you want to stop using the assistant.

Say "Apagar gpt" to permanently turn off the assistant (it will no longer start even if you say "Hola gpt").

## Limitations

Currently, the assistant is only guaranteed to work correctly in Spanish. However, support for many more languages is coming soon.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.