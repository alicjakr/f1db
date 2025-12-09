CREATE TABLE IF NOT EXISTS drivers (
    number INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    team VARCHAR(255) NOT NULL,
    current_points INT
);

INSERT INTO drivers VALUES (
    (1, 'Max', 'Verstappen', 'Red Bull Racing', 421),
    (4, 'Lando', 'Norris', 'McLaren', 423),
    (81, 'Oscar', 'Piastri', 'McLaren', 410),
    (63, 'George', 'Russel', 'Mercedes', 319),
    (16, 'Charles', 'Leclerc', 'Ferrari', 242),
    (5, 'Gabriel', 'Bortoleto', 'Sauber', 19),
    (6, 'Isack', 'Hadjar', 'Racing Bulls', 51),
    (7, 'Jack', 'Doohan', 'Alpine', 0),
    (10, 'Pierre', 'Gasly', 'Alpine', 22),
    (12, 'Andrea Kimi', 'Antonelli', 'Mercedes', 150),
    (14, 'Fernando', 'Alonso', 'Aston Martin Racing', 56),
    (18, 'Lance', 'Stroll', 'Aston Martin Racing', 33),
    (22, 'Yuki', 'Tsunoda', 'Red Bull Racing', 33),
    (23, 'Alex', 'Albon', 'Williams', 73),
    (27, 'Nico', 'Hulkenberg', 'Sauber', 51),
    (30, 'Liam', 'Lawson', 'Racing Bulls', 38),
    (31, 'Esteban', 'Ocon', 'Haas F1 Team', 38),
    (43, 'Franco', 'Colapinto', 'Alpine', 0),
    (44, 'Lewis', 'Hamilton', 'Ferrari', 156),
    (55, 'Carlos', 'Sainz', 'Williams', 64),
    (87, 'Oliver', 'Bearman', 'Haas F1 Team', 41)
);

CREATE TABLE races IF NOT EXISTS (
    round_number INT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    track_name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    distance FLOAT(3) NOT NULL,
    circuit_length FLOAT(3) NOT NULL,
    laps_number INT NOT NULL
);

INSERT INTO races VALUES (
    (1, 'Australia', 'FORMULA 1 LOUIS VUITTON AUSTRALIAN GRAND PRIX 2025', '2025-03-14', '2025-03-16', 306.124, 5.278, 58),
    (2, 'China', 'FORMULA 1 HEINEKEN CHINESE GRAND PRIX 2025', '2025-03-21', '2025-03-23', 305.066, 5.451, 56), --sprint
    (3, 'Japan', 'FORMULA 1 LENOVO JAPANESE GRAND PRIX 2025', '2025-04-04', '2025-04-06', 307.471, 5.807, 53),
    (4, 'Bahrain' 'FORMULA 1 GULF AIR BAHRAIN GRAND PRIX 2025', '2025-04-11', '2025-04-13', 308.238, 5.412, 57),
    (5, 'Saudi Arabia', 'FORMULA 1 STC SAUDI ARABIAN GRAND PRIX 2025', '2025-04-18', '2025-04-20', 308.45, 6.174, 50),
    (6, 'Miami', 'FORMULA 1 CRYPTO.COM MIAMI GRAND PRIX 2025', '2025-05-02', '2025-05-04', 308.326, 5.412, 57), --sprint
    (7, 'Emilia-Romagna', 'FORMULA 1 AWS GRAN PREMIO DEL MADE IN ITALY E DELL\'EMILIA-ROMAGNA 2025', '2025-05-16', '2025-05-18', 309.049, 4.909, 63),
    (8, 'Monaco', 'FORMULA 1 TAG HEUER GRAND PRIX DE MONACO 2025', '2025-05-23', '2025-05-25', 260.286, 3.337, 78),
    (9, 'Spain', 'FORMULA 1 ARAMCO GRAN PREMIO DE ESPAÑA 2025', '2025-05-30', '2025-06-01', 307.236, 4.657, 66),
    (10, 'Canada', 'FORMULA 1 PIRELLI GRAND PRIX DU CANADA 2025', '2025-06-13', '2025-06-15', 305.27, 4.361, 70),
    (11, 'Austria', 'FORMULA 1 MSC CRUISES AUSTRIAN GRAND PRIX 2025', '2025-06-27', '2025-06-29', 307.018, 4.326, 71),
    (12, 'Great Britain', 'FORMULA 1 QATAR AIRWAYS BRITISH GRAND PRIX 2025', '2025-07-04', '2025-07-06', 306.198, 5.891, 52),
    (13, 'Belgium', 'FORMULA 1 MOËT & CHANDON BELGIAN GRAND PRIX 2025', '2025-07-25', '2025-07-27', 308.052, 7.004, 44), --sprint
    (14, 'Hungary', 'FORMULA 1 LENOVO HUNGARIAN GRAND PRIX 2025', '2025-08-01', '2025-08-03', 306.63, 4.381, 70),
    (15, 'Netherlands', 'FORMULA 1 HEINEKEN DUTCH GRAND PRIX 2025', '2025-08-29', '2025-08-31', 306.587, 4.259, 72),
    (16, 'Italy', 'FORMULA 1 PIRELLI GRAN PREMIO D\'ITALIA 2025', '2025-09-05', '2025-09-07', 306.72, 5.793, 53),
    (17, 'Azerbaijan', 'FORMULA 1 QATAR AIRWAYS AZERBAIJAN GRAND PRIX 2025', '2025-09-19', '2025-09-21', 306.049, 6.003, 51),
    (18, 'Singapore', 'FORMULA 1 SINGAPORE AIRLINES SINGAPORE GRAND PRIX 2025', '2025-10-03', '2025-10-05', 305.337, 4.927, 62),
    (19, 'United States', 'FORMULA 1 MSC CRUISES UNITED STATES GRAND PRIX 2025' '2025-10-17', '2025-10-19', 308.405, 5.513, 56), --sprint
    (20, 'Mexico', 'FORMULA 1 GRAN PREMIO DE LA CIUDAD DE MÉXICO 2025', '2025-10-24', '2025-10-26', 305.354, 4.304, 71),
    (21, 'Brazil', 'FORMULA 1 MSC CRUISES GRANDE PRÊMIO DE SÃO PAULO 2025', '2025-11-07', '2025-11-09', 305.879, 4.309, 71), --sprint
    (22, 'Las Vegas', 'FORMULA 1 HEINEKEN LAS VEGAS GRAND PRIX 2025', '2025-11-20', '2025-11-22', 309.958, 6.201, 50),
    (23, 'Qatar', 'FORMULA 1 QATAR AIRWAYS QATAR GRAND PRIX 2025', '2025-11-28', '2025-11-30', 308.611, 5.419, 57), --sprint
    (24, 'Abu Dhabi', 'FORMULA 1 ETIHAD AIRWAYS ABU DHABI GRAND PRIX 2025', '2025-12-05', '2025-12-07', 306.183, 5.281, 58)
);