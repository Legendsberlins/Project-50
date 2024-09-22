SELECT title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.idWHERE people.name = 'Bradley Cooper' AND title in
(SELECT title FROM movies JOIN stars on movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id WHERE people.name = 'Jennifer Lawrence');