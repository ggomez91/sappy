# Sappy

This program can open a SAP GUI, connect to a server, login and optionally open a _tcode_.
Right now it is ad-hoc for my personal SAP configuration but it is easy to customize for others.
Sappy runs on python3 and requires these external libraries:

- _hydra_: Config loading
- _win10toast_: Notifications
- _pyautogui_: Automation

## Config file

Sappy uses [Hydra](https://engineering.fb.com/open-source/hydra/) to load configuration. The config contains the login information and an optional default **tcode**.

```yaml
sap:
  user: ******
  password: ****
  tcode: null
```

## Usage

Just run the script and optionally override the config. ie:

```bash
$ python sap.py sap.tcode=CAT2
```

This runs the CAT2 transaction after log in.

> 💡 You can create Windows shortcuts to make easy access.

## Contribution

Any PR is welcome but I am trying to make this as generic as possible. Before branching from this repo pelase consider how could we integrate new functionality into this one. 😄
