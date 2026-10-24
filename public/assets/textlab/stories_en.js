/* Histórias-base do TextLab (inglês). Cada evento: [sujeito, verbo, objeto, complemento, passiva]
 * sujeito: A (personagem principal), B (segundo personagem), G (grupo, plural)
 * passiva: 1 = objeto singular pode virar sujeito ("The report was written by…"), 2 = plural, 0 = não.
 * Evite expressões de tempo no complemento: os marcadores vêm da estrutura escolhida.
 */
(function (root) {
  'use strict';
  const person = (name, pron) => ({ name, pron, person: pron === 'they' ? 'pl' : pron === 'I' ? '1s' : '3s' });
  // pairs: causa → consequência para as condicionais ([s, v, o, r, s2, v2, o2, r2]).
  const ev = (s, v, o, r, P) => ({ s, v, o, r, pass: P ? o : null, passPl: P === 2 });
  const story = (id, label, title, people, rows, pairs) => ({
    id, label, title, people,
    events: rows.map(([s, v, o, r, P]) => ev(s, v, o, r, P)),
    pairs: (pairs || []).map(([s, v, o, r, s2, v2, o2, r2]) => [ev(s, v, o, r, 0), ev(s2, v2, o2, r2, 0)]),
  });

  const STORIES = [
    story('office', 'Trabalho e escritório', 'A day at the office',
      { A: person('Daniel', 'he'), B: person('Laura', 'she'), G: person("Daniel's team", 'they') }, [
        ['A', 'take', 'the train', 'to the office', 0], ['A', 'check', 'the emails', 'at his desk', 2], ['B', 'call', 'the clients', 'from the meeting room', 2],
        ['A', 'write', 'the weekly report', 'for the manager', 1], ['G', 'prepare', 'the presentation', 'for the meeting', 1], ['A', 'meet', 'Laura', 'in the kitchen', 0],
        ['B', 'make', 'coffee', 'for everyone', 1], ['G', 'discuss', 'the new project', 'in the meeting room', 1], ['B', 'send', 'the contract', 'to the clients', 1],
        ['A', 'finish', 'the report', 'at his desk', 1], ['G', 'have', 'lunch', 'together', 0], ['A', 'go', 'home', 'by bus', 0],
      ], [
        ['A', 'wake up', '', 'late', 'A', 'miss', 'the train', ''], ['A', 'miss', 'the train', '', 'A', 'arrive', '', 'late to work'],
        ['G', 'finish', 'the presentation', 'early', 'G', 'have', 'more time', 'for questions'], ['A', 'write', 'the report', 'tonight', 'B', 'read', 'it', 'in the morning'],
      ]),
    story('school', 'Escola e estudos', "Sofia's school day",
      { A: person('Sofia', 'she'), B: person('Mr. Carter', 'he'), G: person("Sofia's classmates", 'they') }, [
        ['A', 'ride', 'her bike', 'to school', 0], ['B', 'explain', 'the lesson', 'to the class', 1], ['G', 'read', 'a short story', 'in English', 1],
        ['A', 'take', 'notes', 'in her notebook', 2], ['G', 'work', '', 'in small groups', 0], ['A', 'answer', "the teacher's questions", 'in class', 2],
        ['B', 'correct', 'the tests', 'in the staff room', 2], ['A', 'study', '', 'for the exam in the library', 0], ['G', 'play', 'basketball', 'at break', 0],
        ['B', 'give', 'extra exercises', 'to the students', 2], ['A', 'practice', 'the new words', 'with a friend', 2], ['G', 'present', 'their project', 'to the class', 0],
      ], [
        ['A', 'study', '', 'hard', 'A', 'pass', 'the exam', ''], ['G', 'work', '', 'together', 'G', 'finish', 'the project', 'faster'],
        ['B', 'explain', 'the lesson', 'again', 'A', 'understand', 'it', 'better'], ['A', 'practice', 'the new words', 'every day', 'A', 'remember', 'them', 'easily'],
      ]),
    story('travel', 'Viagem', 'A trip to the coast',
      { A: person('Lucas', 'he'), B: person('Mia', 'she'), G: person('their parents', 'they') }, [
        ['G', 'book', 'a hotel', 'near the beach', 1], ['A', 'pack', 'the suitcases', 'carefully', 2], ['B', 'buy', 'the train tickets', 'online', 2],
        ['G', 'drive', '', 'to the station', 0], ['A', 'carry', 'the heavy bags', 'to the car', 2], ['B', 'take', 'photos', 'of the sea', 0],
        ['A', 'swim', '', 'in the sea', 0], ['G', 'rent', 'bikes', 'in town', 2], ['B', 'visit', 'the old lighthouse', 'with her brother', 1],
        ['A', 'try', 'the local food', 'at a small restaurant', 1], ['G', 'walk', '', 'along the beach', 0], ['B', 'send', 'postcards', 'to her friends', 2],
        ['A', 'watch', 'the sunset', 'from the hotel balcony', 1],
      ], [
        ['B', 'buy', 'the tickets', 'online', 'G', 'save', 'money', ''], ['A', 'pack', '', 'light', 'A', 'carry', 'the bags', 'easily'],
        ['G', 'rent', 'bikes', '', 'G', 'see', 'more of the town', ''], ['A', 'wake up', '', 'early', 'A', 'watch', 'the sunrise', 'from the beach'],
      ]),
    story('home', 'Casa e família', 'Busy at home',
      { A: person('Emma', 'she'), B: person('Tom', 'he'), G: person('the kids', 'they') }, [
        ['A', 'cook', 'dinner', 'for the family', 1], ['B', 'wash', 'the dishes', 'in the kitchen', 2], ['G', 'clean', 'their rooms', '', 0],
        ['A', 'water', 'the plants', 'in the garden', 2], ['B', 'fix', 'the kitchen door', '', 1], ['G', 'set', 'the table', 'for dinner', 1],
        ['A', 'read', 'a story', 'to the kids', 1], ['B', 'take', 'the dog', 'for a walk', 0], ['G', 'feed', 'the cat', '', 1],
        ['A', 'organize', 'the cupboards', '', 2], ['B', 'paint', 'the fence', 'in the backyard', 1], ['G', 'help', 'their parents', 'with the shopping', 0],
      ], [
        ['A', 'cook', 'dinner', 'early', 'G', 'eat', '', 'together'], ['G', 'clean', 'their rooms', '', 'A', 'take', 'them', 'to the park'],
        ['A', 'water', 'the plants', 'every day', 'A', 'have', 'beautiful flowers', 'in spring'], ['B', 'fix', 'the door', '', 'G', 'sleep', '', 'better'],
      ]),
    story('sport', 'Esporte e saúde', 'Training for a race',
      { A: person('Ana', 'she'), B: person('Coach Ryan', 'he'), G: person("Ana's teammates", 'they') }, [
        ['A', 'run', 'five kilometers', 'in the park', 0], ['B', 'plan', 'the training sessions', 'for the team', 2], ['G', 'stretch', '', 'before practice', 0],
        ['A', 'drink', 'a lot of water', 'during practice', 0], ['B', 'check', 'the times', 'with a stopwatch', 2], ['G', 'lift', 'weights', 'at the gym', 0],
        ['A', 'eat', 'a healthy breakfast', '', 0], ['B', 'organize', 'a friendly race', 'for the club', 1], ['A', 'win', 'the race', '', 1],
        ['G', 'cheer', '', 'for their friend', 0], ['A', 'rest', '', 'at home', 0], ['B', 'record', 'the results', 'in a notebook', 2],
      ], [
        ['A', 'train', '', 'every day', 'A', 'win', 'the race', ''], ['A', 'sleep', '', 'well', 'A', 'feel', '', 'stronger'],
        ['B', 'plan', 'the sessions', 'carefully', 'G', 'improve', '', 'quickly'], ['A', 'drink', 'enough water', '', 'A', 'run', '', 'faster'],
      ]),
    story('city', 'Cidade e compras', 'Saturday in the city',
      { A: person('Ben', 'he'), B: person('Julia', 'she'), G: person("Ben's friends", 'they') }, [
        ['A', 'meet', 'his friends', 'downtown', 0], ['B', 'buy', 'a new jacket', 'at the mall', 1], ['G', 'look', '', 'for a good restaurant', 0],
        ['A', 'pay', 'the bill', 'at the restaurant', 1], ['B', 'choose', 'a present', 'for her mother', 1], ['G', 'visit', 'the art museum', 'downtown', 1],
        ['A', 'take', 'the subway', 'home', 0], ['B', 'compare', 'prices', 'online', 2], ['G', 'watch', 'a movie', 'at the cinema', 1],
        ['A', 'carry', 'the shopping bags', 'to the car', 2], ['B', 'order', 'pizza', 'for everyone', 1], ['G', 'walk', '', 'around the old town', 0],
      ], [
        ['A', 'take', 'the subway', '', 'A', 'arrive', '', 'on time'], ['B', 'find', 'a good jacket', '', 'B', 'buy', 'it', ''],
        ['G', 'book', 'a table', '', 'G', 'get', 'a good seat', ''], ['A', 'save', 'money', 'this month', 'A', 'buy', 'new shoes', ''],
      ]),
    story('tech', 'Tecnologia', 'Launching a new app',
      { A: person('Priya', 'she'), B: person('Leo', 'he'), G: person('the developers', 'they') }, [
        ['A', 'design', 'the new app', 'on her laptop', 1], ['B', 'test', 'the login page', 'on his phone', 1], ['G', 'write', 'the code', 'in small parts', 1],
        ['A', 'fix', 'the bugs', 'quickly', 2], ['B', 'update', 'the website', '', 1], ['G', 'install', 'the new software', 'on every computer', 1],
        ['A', 'present', 'the app', 'to the clients', 1], ['B', 'answer', "the users' questions", 'by email', 2], ['G', 'review', 'the design', 'together', 1],
        ['A', 'save', 'the files', 'in the cloud', 2], ['B', 'back up', 'the data', '', 1], ['G', 'celebrate', 'the launch', 'with cake', 1],
      ], [
        ['B', 'test', 'the app', 'carefully', 'G', 'find', 'the bugs', 'quickly'], ['A', 'fix', 'the bugs', 'today', 'G', 'launch', 'the app', 'tomorrow'],
        ['G', 'write', 'clear code', '', 'B', 'understand', 'it', 'easily'], ['A', 'save', 'the files', 'in the cloud', 'A', 'never lose', 'her work', ''],
      ]),
    story('restaurant', 'Restaurante', 'A busy night at the restaurant',
      { A: person('Carlos', 'he'), B: person('Nina', 'she'), G: person('the customers', 'they') }, [
        ['A', 'prepare', 'the sauce', 'in the kitchen', 1], ['B', 'welcome', 'the guests', 'at the door', 2], ['G', 'read', 'the menu', 'carefully', 1],
        ['B', 'take', 'the orders', 'at every table', 2], ['A', 'cut', 'the vegetables', 'for the soup', 2], ['G', 'order', 'the special dish', '', 1],
        ['A', 'bake', 'fresh bread', 'in the oven', 1], ['B', 'serve', 'the food', 'with a smile', 1], ['G', 'enjoy', 'the meal', '', 1],
        ['B', 'bring', 'the bill', 'to the table', 1], ['G', 'leave', 'a big tip', 'for the staff', 1], ['A', 'clean', 'the kitchen', 'carefully', 1],
      ], [
        ['A', 'buy', 'fresh vegetables', '', 'A', 'make', 'a better soup', ''], ['B', 'work', '', 'quickly', 'G', 'get', 'their food', 'sooner'],
        ['G', 'enjoy', 'the meal', '', 'G', 'leave', 'a big tip', ''], ['A', 'bake', 'more bread', '', 'B', 'serve', 'it', 'with the soup'],
      ]),
    story('community', 'Comunidade e meio ambiente', 'A greener neighborhood',
      { A: person('Grace', 'she'), B: person('Omar', 'he'), G: person('the volunteers', 'they') }, [
        ['G', 'plant', 'trees', 'in the park', 2], ['A', 'collect', 'plastic bottles', 'in the square', 2], ['B', 'build', 'a small garden', 'behind the school', 1],
        ['G', 'paint', 'the old wall', 'with bright colors', 1], ['A', 'organize', 'a cleanup day', 'for the neighbors', 1], ['B', 'repair', 'the broken benches', 'in the square', 2],
        ['G', 'pick up', 'the trash', 'along the river', 1], ['A', 'give', 'a short talk', 'at the community center', 1], ['B', 'recycle', 'old paper', 'at home', 1],
        ['G', 'share', 'the photos', 'online', 2], ['A', 'thank', 'the volunteers', 'for their help', 2], ['B', 'sell', 'vegetables', 'at the local market', 2],
      ], [
        ['G', 'plant', 'more trees', '', 'G', 'have', 'more shade', 'in the park'], ['A', 'organize', 'a cleanup day', '', 'B', 'help', 'her', ''],
        ['B', 'repair', 'the benches', '', 'A', 'sit', '', 'in the square'], ['G', 'recycle', 'more paper', '', 'G', 'save', 'a lot of trees', ''],
      ]),
    story('party', 'Festa e celebrações', "Lily's birthday party",
      { A: person('Jake', 'he'), B: person('Lily', 'she'), G: person('their friends', 'they') }, [
        ['A', 'plan', 'a surprise party', 'for Lily', 1], ['G', 'decorate', 'the living room', 'with balloons', 1], ['A', 'bake', 'a chocolate cake', '', 1],
        ['G', 'bring', 'presents', 'for Lily', 2], ['B', 'open', 'the door', '', 1], ['G', 'sing', '"Happy Birthday"', 'together', 1],
        ['B', 'blow out', 'the candles', '', 2], ['A', 'take', 'pictures', 'of everyone', 0], ['G', 'dance', '', 'in the living room', 0],
        ['B', 'open', 'the presents', '', 2], ['A', 'clean', 'the house', 'after the party', 1], ['G', 'eat', 'the cake', '', 1],
      ], [
        ['A', 'bake', 'a cake', '', 'B', 'be', '', 'very happy'], ['G', 'arrive', '', 'early', 'G', 'help', 'Jake', 'with the decorations'],
        ['B', 'open', 'the presents', 'now', 'G', 'take', 'pictures', ''], ['A', 'play', 'music', '', 'G', 'dance', '', 'all night'],
      ]),
  ];

  if (typeof module === 'object' && module.exports) module.exports = STORIES;
  else root.TEXTLAB_STORIES = STORIES;
})(typeof window !== 'undefined' ? window : globalThis);
