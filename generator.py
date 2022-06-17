import math

right_skills = ["Python", "Elastic search", "Docker", "Apache Spark", "Apache Hadoop",
                "Linux", "Apache NiFi", "Apache Airflow", "Apache Kafka", "Kubernetes",
                "GitLab CI/CD", "Rabbitmq", "SQL", "Flask", "Django", "MongoDB",
                "Rabbitmq", "Git"]
right_skills = ['Python', "SQL", "Clustering", "Classifica tion", "Jupyter Notebook"]

colors = ["e95a93", "e95a93", "ffc300", "2ec4b6"]
delay = 0.02
background_color = 111

angel = 0
radius = 120
base = 15
ratio = 4

color_index = 0
color = colors[0]

for_color = '3a0ca3'


def get_point(radius, angle):
    angle = math.pi * 2 * (angle / 360)
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    return int(x), int(y)


once = True
for i, item in enumerate(right_skills):
    if angel >= 360:
        color_index += 1
        color = colors[color_index]
        ratio -= 2
        radius += 120
    angel = angel % 360
    left, top = get_point(radius=radius, angle=angel)
    # print(radius, angel, top, left, item, )

    delay += 0.12
    angel += base * ratio  # first 45
    background_color += 20
    # item_width = int(((len(item) / 6) + 1) * 50)
    item_width = 100

    template = F"""
    <a class='tab' href='#'
               style="
                      width: {item_width}px;
                      padding-bottom: 100px;
                      height: 50px;
                      font-size: 12px;
                      top: {top}px;
                      left: {left}px;
                      color: #{for_color};
                      background-color: #{color};
                      transition-delay: {str(delay)}s;">
                <p>{item}</p>
    </a>
    """

    print(template)
