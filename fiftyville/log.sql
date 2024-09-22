-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports; -- To view all the records
SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7; -- Narrow down search #295
SELECT * FROM interviews WHERE day = 28 AND month = 7; -- Analyze transcripts
SELECT * FROM bakery_security_logs WHERE day = 28 AND hour = 10 AND minute > 15; --Narrow down bakery search
SELECT * FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 60;


SELECT * FROM flights JOIN airports ON airports.id = flights.origin_airport_id WHERE day = 29 AND month = 7; -- Narrow airports search

SELECT name, license_plate,atm_transactions.account_number FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.month = 7 AND atm_transactions.day = 28 AND atm_transactions.atm_location = 'Leggett Street' AND atm_transactions.transaction_type = 'withdraw';

SELECT name, people.passport_number ,bakery_security_logs.license_plate FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 15;

SELECT airports.full_name, passengers.passport_number FROM airports
JOIN flights ON flights.origin_airport_id = airports.id
JOIN passengers ON passengers.flight_id = flights.id WHERE flights.day = 29 AND flights.month = 7 AND flights.hour = 8;

SELECT people.name, phone_calls.caller FROM people
JOIN phone_calls ON phone_calls.caller = people.phone_number WHERE phone_calls.day = 28 AND phone_calls.month = 7 AND phone_calls.duration < 60; --Bruce


SELECT people.name, phone_calls.caller, phone_calls.receiver FROM people
JOIN phone_calls ON phone_calls.caller = people.phone_number WHERE people.name = 'Bruce' AND phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration < 60; --Robin


