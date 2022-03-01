# Message Russian people through reviews.

There has been an initiative to help Russian people overcome censorship and get real information about what is going on
in Ukraine by writing reviews on Google Maps and similar. This tool automates this job (almost) completely, making it
much easier to reach more people.

It supports Yandex.ru so far, as this should be the most popular review website in Russia. Feel free to add more modules
and functionalities.

## First run

1. Make sure you have Google Chrome installed (support for another browser might be added later).
2. Download correct version of Chromedriver from https://chromedriver.chromium.org/downloads
3. Create file `settings.py` based on `settings_example.py` and set values accordingly.
4. Prepare an account to comment (Google, Yandex or other).
5. Run.

## Each other run

1. Browser window opens automatically.
2. Login (for example with your fake gmail account).
3. Navigate to: https://yandex.ru/maps
4. Navigate to random area in Russia
5. Search for a venue type (for example `ресторан` for `restaurant`)
6. Press Enter and enjoy (this might be automated a bit more in the future, but it really should not take too much
   effort.)
