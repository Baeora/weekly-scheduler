
# Weekly Calendar Scheduler

## Greeting
Hello! I made this repo to serve as a tool for myself in order to help create a unique weekly schedule that I can use as a starting point to build a week that doesn't involve me playing video games for hours a day

I hope it helps you!

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Version Notes](#version-notes)
- [License](#license)

## Overview
This tool takes in a prompt from the file `prompt.py` and feeds it into the OpenAI GPT via the API, and uses the return as a list of dictionary events that are then fed into Google Calendar via the Calendar API

## Installation

### Preparation
Before installing, complete the following tasks:

- (For beginners) Make sure [Python](https://www.python.org/downloads/) and [PIP](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/) are added to [PATH](https://realpython.com/add-python-to-path/).

	- During your Python install, you can specify that you'd like to do this by choosing Custom Installation, highly recommend!

	- You'll also need an IDE to code in, I use [VSCode](https://code.visualstudio.com/download).

- Get your [OpenAI API Key](https://openai.com/index/openai-api/)!
  - Create an OpenAI Account
  - In the top left, make a new project with your desired project name
  - Head to your [Profile](https://platform.openai.com/settings/profile) and under the `Your Profile` section click the `User API Keys` tab
  - Create a new `Project API Key` from here

- Obtain Google [Oauth2](https://console.cloud.google.com/projectselector2/apis/credentials?supportedpurview=project) credentials (JSON format).

	- Make sure to add the Calendar API to your project!!
  - Make a `Service Account` as those are the credentials you'll need
  - Might need to google this if you're unfamiliar

  
### Install
Once you have finished the above tasks, navigate to the directory you'd like to work in and do the following:

- Clone this repository

	```git clone https://github.com/Baeora/weekly-scheduler.git```

- Inside said repository, use PipEnv to install dependencies

	```pipenv sync```

- Put your Google Calendar `SERVICE FILE CREDENTIALS` in the `parent` directory

- Navigate to the parent directory and create a `.env` file with the following information:
  - `OPENAI_API_KEY = '<Your OpenAI API Key>'`
  - `CALENDAR_ID = '<The Calendar ID of the Calendar you'd like to create events in>'`

That **should** be everything. If you run into errors or spot anything that I missed, please reach out!

## License
MIT License

Copyright (c) 2024 Beora

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
