#Japan Backbone Network
class Net:
    def __init__(self):
        self.network=[['Sapporo', 'Aomori', 'Morioka', 'Sendai', 'Akita', 'Yamagata', 'Fukushima', 'Mito', 'Utsunomiya',
                       'Maebashi', 'Omiya', 'Chiba', 'Tokyo', 'Hachioji', 'Yokohama', 'Niigata', 'Toyama', 'Kanazawa',
                       'Fukui', 'Kofu', 'Nagano', 'Gifu', 'Shizuoka', 'Nagoya', 'Tsu', 'Otsu', 'Kyoto',
                       'Osaka', 'Kobe', 'Nara','Wakayama', 'Tottori', 'Matsue', 'Okayama', 'Hiroshima', 'Yamaguchi',
                       'Tokushima', 'Takamatsu', 'Matsuyama', 'Kochi', 'Hakata', 'Saga', 'Nagasaki', 'Kumamoto', 'Oita',
                       'Miyazaki', 'Kagoshima', 'Naha'],
                      [('Sapporo', 'Aomori'), ('Sapporo', 'Morioka'), ('Aomori', 'Morioka'), ('Aomori', 'Akita'), ('Morioka', 'Akita'), ('Morioka', 'Sendai'),
                       ('Akita', 'Yamagata'), ('Sendai', 'Yamagata'), ('Akita', 'Niigata'), ('Yamagata', 'Niigata'), ('Sendai', 'Fukushima'), ('Sendai', 'Mito'),
                       ('Fukushima', 'Niigata'), ('Fukushima', 'Utsunomiya'), ('Utsunomiya', 'Mito'), ('Mito', 'Chiba'), ('Mito', 'Omiya'), ('Utsunomiya', 'Omiya'),
                       ('Utsunomiya', 'Maebashi'), ('Omiya', 'Chiba'), ('Maebashi', 'Omiya'), ('Chiba', 'Tokyo'), ('Omiya', 'Tokyo'), ('Tokyo', 'Yokohama'),
                       ('Tokyo', 'Hachioji'), ('Hachioji', 'Yokohama'), ('Maebashi', 'Hachioji'), ('Yokohama', 'Shizuoka'), ('Hachioji', 'Kofu'), ('Maebashi', 'Nagano'),
                       ('Kofu', 'Shizuoka'), ('Maebashi', 'Niigata'), ('Niigata', 'Toyama'), ('Niigata', 'Nagano'), ('Kofu', 'Nagano'), ('Toyama', 'Kanazawa'),
                       ('Toyama', 'Nagano'), ('Nagano', 'Nagoya'), ('Kofu', 'Nagoya'), ('Shizuoka', 'Nagoya'), ('Kanazawa', 'Fukui'), ('Fukui', 'Kyoto'),
                       ('Gifu', 'Nagoya'), ('Gifu', 'Otsu'), ('Nagoya', 'Tsu'), ('Tsu', 'Otsu'), ('Tsu', 'Wakayama'), ('Tsu', 'Nara'),
                       ('Otsu', 'Kyoto'), ('Kyoto', 'Nara'), ('Osaka', 'Nara'), ('Kyoto', 'Osaka'), ('Kyoto', 'Tottori'), ('Kyoto', 'Kobe'),
                       ('Osaka', 'Kobe'), ('Osaka', 'Wakayama'), ('Kobe', 'Okayama'), ('Tokushima', 'Takamatsu'), ('Okayama', 'Takamatsu'), ('Wakayama', 'Tokushima'),
                       ('Tokushima', 'Kochi'), ('Takamatsu', 'Kochi'), ('Tottori', 'Okayama'), ('Takamatsu', 'Matsuyama'), ('Okayama', 'Hiroshima'), ('Tottori', 'Matsue'),
                       ('Matsuyama', 'Kochi'), ('Matsue', 'Yamaguchi'), ('Hiroshima', 'Yamaguchi'), ('Hiroshima', 'Matsuyama'), ('Matsuyama', 'Oita'), ('Yamaguchi', 'Hakata'),
                       ('Hakata', 'Oita'), ('Hakata', 'Saga'), ('Hakata', 'Kumamoto'), ('Kumamoto', 'Oita'), ('Oita', 'Miyazaki'), ('Saga', 'Nagasaki'),
                       ('Kumamoto', 'Kagoshima'), ('Miyazaki', 'Kagoshima'), ('Nagasaki', 'Naha'), ('Kagoshima', 'Naha'),
                       ('Naha', 'Kagoshima'),
                       ('Naha', 'Nagasaki'),
                       ('Kagoshima', 'Miyazaki'),
                       ('Kagoshima', 'Kumamoto'),
                       ('Nagasaki', 'Saga'),
                       ('Miyazaki', 'Oita'),
                       ('Oita', 'Kumamoto'),
                       ('Kumamoto', 'Hakata'),
                       ('Saga', 'Hakata'),
                       ('Oita', 'Hakata'),
                       ('Hakata', 'Yamaguchi'),
                       ('Oita', 'Matsuyama'),
                       ('Matsuyama', 'Hiroshima'),
                       ('Yamaguchi', 'Hiroshima'),
                       ('Yamaguchi', 'Matsue'),
                       ('Kochi', 'Matsuyama'),
                       ('Matsue', 'Tottori'),
                       ('Hiroshima', 'Okayama'),
                       ('Matsuyama', 'Takamatsu'),
                       ('Okayama', 'Tottori'),
                       ('Kochi', 'Takamatsu'),
                       ('Kochi', 'Tokushima'),
                       ('Tokushima', 'Wakayama'),
                       ('Takamatsu', 'Okayama'),
                       ('Takamatsu', 'Tokushima'),
                       ('Okayama', 'Kobe'),
                       ('Wakayama', 'Osaka'),
                       ('Kobe', 'Osaka'),
                       ('Kobe', 'Kyoto'),
                       ('Tottori', 'Kyoto'),
                       ('Osaka', 'Kyoto'),
                       ('Nara', 'Osaka'),
                       ('Nara', 'Kyoto'),
                       ('Kyoto', 'Otsu'),
                       ('Nara', 'Tsu'),
                       ('Wakayama', 'Tsu'),
                       ('Otsu', 'Tsu'),
                       ('Tsu', 'Nagoya'),
                       ('Otsu', 'Gifu'),
                       ('Nagoya', 'Gifu'),
                       ('Kyoto', 'Fukui'),
                       ('Fukui', 'Kanazawa'),
                       ('Nagoya', 'Shizuoka'),
                       ('Nagoya', 'Kofu'),
                       ('Nagoya', 'Nagano'),
                       ('Nagano', 'Toyama'),
                       ('Kanazawa', 'Toyama'),
                       ('Nagano', 'Kofu'),
                       ('Nagano', 'Niigata'),
                       ('Toyama', 'Niigata'),
                       ('Niigata', 'Maebashi'),
                       ('Shizuoka', 'Kofu'),
                       ('Nagano', 'Maebashi'),
                       ('Kofu', 'Hachioji'),
                       ('Shizuoka', 'Yokohama'),
                       ('Hachioji', 'Maebashi'),
                       ('Yokohama', 'Hachioji'),
                       ('Hachioji', 'Tokyo'),
                       ('Yokohama', 'Tokyo'),
                       ('Tokyo', 'Omiya'),
                       ('Tokyo', 'Chiba'),
                       ('Omiya', 'Maebashi'),
                       ('Chiba', 'Omiya'),
                       ('Maebashi', 'Utsunomiya'),
                       ('Omiya', 'Utsunomiya'),
                       ('Omiya', 'Mito'),
                       ('Chiba', 'Mito'),
                       ('Mito', 'Utsunomiya'),
                       ('Utsunomiya', 'Fukushima'),
                       ('Niigata', 'Fukushima'),
                       ('Mito', 'Sendai'),
                       ('Fukushima', 'Sendai'),
                       ('Niigata', 'Yamagata'),
                       ('Niigata', 'Akita'),
                       ('Yamagata', 'Sendai'),
                       ('Yamagata', 'Akita'),
                       ('Sendai', 'Morioka'),
                       ('Akita', 'Morioka'),
                       ('Akita', 'Aomori'),
                       ('Morioka', 'Aomori'),
                       ('Morioka', 'Sapporo'),
                       ('Aomori', 'Sapporo')
                       ]]

        self.leftset=[0,1,2,3,4,33,34,35,36,37,38]
        self.rightset=[5
,6
,7
,8
,9
,10
,11
,12
,13
,14
,15
,16
,17
,18
,19
,20
,21
,22
,23
,24
,25
,26
,27
,28
,29
,30
,31
,32
]

# #US Backbone network
# class Net:
#     def __init__(self):
#         self.network=[['Vancouver', 'LosAngeles', 'SanFrancisco', 'LasVegas', 'SaltLakeCity', 'ElPaso', 'Dallas', 'Houston',
#                  'OklahomaCity', 'Minneapolis', 'KansasCity', 'Denver', 'Chicago', 'Indianapolis', 'Detroit', 'StLouis',
#                  'Nashville', 'Cleveland', 'NewYork', 'Montreal', 'Charlotte', 'NewOrleans', 'Boston', 'Atlanta',
#                  'Miami',
#                  'WashingtonDC', 'Philadelphia', 'Toronto', 'Pittsburgh', 'Cincinnati', 'Tampa', 'Memphis', 'Winnipeg',
#                  'Calgary', 'Seattle', 'Portland', 'Sacrameto', 'Phoenix', 'SanDiego'],[('Vancouver', 'Calgary'), ('Vancouver', 'Seattle'), ('LosAngeles', 'SanFrancisco'),
#                  ('LosAngeles', 'LasVegas'),
#                  ('LosAngeles', 'SanDiego'), ('SanFrancisco', 'LosAngeles'), ('SanFrancisco', 'Portland'),
#                  ('SanFrancisco', 'Sacrameto'), ('LasVegas', 'LosAngeles'), ('LasVegas', 'SaltLakeCity'),
#                  ('LasVegas', 'Sacrameto'), ('LasVegas', 'Phoenix'), ('SaltLakeCity', 'LasVegas'),
#                  ('SaltLakeCity', 'Denver'),
#                  ('SaltLakeCity', 'Calgary'), ('SaltLakeCity', 'Portland'), ('SaltLakeCity', 'Sacrameto'),
#                  ('ElPaso', 'Dallas'),
#                  ('ElPaso', 'Houston'), ('ElPaso', 'Phoenix'), ('Dallas', 'ElPaso'), ('Dallas', 'Houston'),
#                  ('Dallas', 'OklahomaCity'), ('Dallas', 'Denver'), ('Dallas', 'Memphis'), ('Houston', 'ElPaso'),
#                  ('Houston', 'Dallas'), ('Houston', 'NewOrleans'), ('OklahomaCity', 'Dallas'),
#                  ('OklahomaCity', 'KansasCity'),
#                  ('Minneapolis', 'KansasCity'), ('Minneapolis', 'Chicago'), ('Minneapolis', 'Winnipeg'),
#                  ('KansasCity', 'OklahomaCity'), ('KansasCity', 'Minneapolis'), ('KansasCity', 'Denver'),
#                  ('KansasCity', 'StLouis'), ('Denver', 'SaltLakeCity'), ('Denver', 'Dallas'), ('Denver', 'KansasCity'),
#                  ('Chicago', 'Minneapolis'), ('Chicago', 'Indianapolis'), ('Chicago', 'Detroit'),
#                  ('Chicago', 'StLouis'),
#                  ('Indianapolis', 'Chicago'), ('Indianapolis', 'StLouis'), ('Indianapolis', 'Nashville'),
#                  ('Indianapolis', 'Cincinnati'), ('Detroit', 'Chicago'), ('Detroit', 'Cleveland'),
#                  ('Detroit', 'Toronto'),
#                  ('StLouis', 'KansasCity'), ('StLouis', 'Chicago'), ('StLouis', 'Indianapolis'), ('StLouis', 'Memphis'),
#                  ('Nashville', 'Indianapolis'), ('Nashville', 'Charlotte'), ('Nashville', 'Atlanta'),
#                  ('Nashville', 'Memphis'),
#                  ('Cleveland', 'Detroit'), ('Cleveland', 'NewYork'), ('Cleveland', 'Pittsburgh'),
#                  ('Cleveland', 'Cincinnati'),
#                  ('NewYork', 'Cleveland'), ('NewYork', 'Boston'), ('NewYork', 'Philadelphia'), ('NewYork', 'Toronto'),
#                  ('Montreal', 'Boston'), ('Montreal', 'Toronto'), ('Charlotte', 'Nashville'), ('Charlotte', 'Atlanta'),
#                  ('Charlotte', 'WashingtonDC'), ('Charlotte', 'Tampa'), ('NewOrleans', 'Houston'),
#                  ('NewOrleans', 'Atlanta'),
#                  ('NewOrleans', 'Miami'), ('NewOrleans', 'Memphis'), ('Boston', 'NewYork'), ('Boston', 'Montreal'),
#                  ('Atlanta', 'Nashville'), ('Atlanta', 'Charlotte'), ('Atlanta', 'NewOrleans'), ('Atlanta', 'Tampa'),
#                  ('Miami', 'NewOrleans'), ('Miami', 'Tampa'), ('WashingtonDC', 'Charlotte'),
#                  ('WashingtonDC', 'Philadelphia'),
#                  ('WashingtonDC', 'Pittsburgh'), ('Philadelphia', 'NewYork'), ('Philadelphia', 'WashingtonDC'),
#                  ('Toronto', 'Detroit'), ('Toronto', 'NewYork'), ('Toronto', 'Montreal'), ('Pittsburgh', 'Cleveland'),
#                  ('Pittsburgh', 'WashingtonDC'), ('Cincinnati', 'Indianapolis'), ('Cincinnati', 'Cleveland'),
#                  ('Tampa', 'Charlotte'), ('Tampa', 'Atlanta'), ('Tampa', 'Miami'), ('Memphis', 'Dallas'),
#                  ('Memphis', 'StLouis'), ('Memphis', 'Nashville'), ('Memphis', 'NewOrleans'),
#                  ('Winnipeg', 'Minneapolis'),
#                  ('Winnipeg', 'Calgary'), ('Calgary', 'Vancouver'), ('Calgary', 'SaltLakeCity'),
#                  ('Calgary', 'Winnipeg'),
#                  ('Seattle', 'Vancouver'), ('Seattle', 'Portland'), ('Portland', 'SanFrancisco'),
#                  ('Portland', 'SaltLakeCity'),
#                  ('Portland', 'Seattle'), ('Sacrameto', 'SanFrancisco'), ('Sacrameto', 'LasVegas'),
#                  ('Sacrameto', 'SaltLakeCity'), ('Phoenix', 'LasVegas'), ('Phoenix', 'ElPaso'), ('Phoenix', 'SanDiego'),
#                  ('SanDiego', 'LosAngeles'), ('SanDiego', 'Phoenix')]]
#
#         self.leftset=[0,1,2,3,4,33,34,35,36,37,38]
#         self.rightset=[5
# ,6
# ,7
# ,8
# ,9
# ,10
# ,11
# ,12
# ,13
# ,14
# ,15
# ,16
# ,17
# ,18
# ,19
# ,20
# ,21
# ,22
# ,23
# ,24
# ,25
# ,26
# ,27
# ,28
# ,29
# ,30
# ,31
# ,32
# ]