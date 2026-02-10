
from datetime import datetime, time

# Conference Info
EVENT_INFO = {
    "name": "Google Cloud Next Gen 2026",
    "date": "February 14, 2026",
    "location": "Expo Tampico, Tampico, Tamaulipas",
    "description": "A deep dive into the future of cloud computing, AI, and infrastructure."
}

# Speakers Data
SPEAKERS = {
    1: {"first": "Alice", "last": "Chen", "linkedin": "https://linkedin.com/in/alicechen", "role": "Cloud Architect"},
    2: {"first": "Bob", "last": "Smith", "linkedin": "https://linkedin.com/in/bobsmith", "role": "Data Engineer"},
    3: {"first": "Charlie", "last": "Davis", "linkedin": "https://linkedin.com/in/charliedavis", "role": "Security Specialist"},
    4: {"first": "Diana", "last": "Prince", "linkedin": "https://linkedin.com/in/dianaprince", "role": "ML Researcher"},
    5: {"first": "Ethan", "last": "Hunt", "linkedin": "https://linkedin.com/in/ethanhunt", "role": "DevOps Lead"},
    6: {"first": "Fiona", "last": "Gallagher", "linkedin": "https://linkedin.com/in/fionagallagher", "role": "Product Manager"},
    7: {"first": "George", "last": "Lucas", "linkedin": "https://linkedin.com/in/georgelucas", "role": "Backend Developer"},
    8: {"first": "Hannah", "last": "Montana", "linkedin": "https://linkedin.com/in/hannahmontana", "role": "Frontend Engineer"},
    9: {"first": "Ian", "last": "Malcolm", "linkedin": "https://linkedin.com/in/ianmalcolm", "role": "Chaos Engineer"},
    10: {"first": "Julia", "last": "Roberts", "linkedin": "https://linkedin.com/in/juliaroberts", "role": "Cloud Consultant"},
}

# Schedule Data
# 8 Talks + 1 Lunch (60 mins)
# Format: ID, Title, SpeakerIDs, Categories, Description, StartTime, EndTime
SCHEDULE = [
    {
        "id": 1,
        "type": "talk",
        "title": "Keynote: The Future of Google Cloud",
        "speaker_ids": [1],
        "categories": ["Keynote", "Cloud Strategy"],
        "description": "Opening remarks on the vision of Google Cloud technologies for the next decade.",
        "start_time": "09:00",
        "end_time": "10:00"
    },
    {
        "id": 2,
        "type": "talk",
        "title": "Scaling with Kubernetes Autopilot",
        "speaker_ids": [2, 5],
        "categories": ["Infrastructure", "Kubernetes"],
        "description": "Learn how to optimize your GKE clusters using Autopilot mode for efficiency and security.",
        "start_time": "10:15",
        "end_time": "11:00"
    },
    {
        "id": 3,
        "type": "talk",
        "title": "Advanced BigQuery Analytics",
        "speaker_ids": [6],
        "categories": ["Data", "Analytics"],
        "description": "Deep dive into BigQuery optimization techniques and new features for real-time analytics.",
        "start_time": "11:15",
        "end_time": "12:00"
    },
    {
        "id": 4,
        "type": "break",
        "title": "Lunch Break",
        "speaker_ids": [],
        "categories": ["Networking"],
        "description": "Catered lunch and networking opportunities.",
        "start_time": "12:00",
        "end_time": "13:00"
    },
    {
        "id": 5,
        "type": "talk",
        "title": "Securing Your Cloud Payload",
        "speaker_ids": [3],
        "categories": ["Security", "Compliance"],
        "description": "Best practices for IAM, VPC Service Controls, and keeping your data safe.",
        "start_time": "13:00",
        "end_time": "13:45"
    },
    {
        "id": 6,
        "type": "talk",
        "title": "Generative AI on Vertex AI",
        "speaker_ids": [4, 10],
        "categories": ["AI/ML", "Generative AI"],
        "description": "Building and deploying LLM applications using Vertex AI and Gemini models.",
        "start_time": "14:00",
        "end_time": "14:45"
    },
    {
        "id": 7,
        "type": "talk",
        "title": "Serverless Architectures with Cloud Run",
        "speaker_ids": [7],
        "categories": ["Serverless", "Application Development"],
        "description": "How to build resilient, scalable web applications without managing servers.",
        "start_time": "15:00",
        "end_time": "15:45"
    },
    {
        "id": 8,
        "type": "talk",
        "title": "Chaos Engineering in the Cloud",
        "speaker_ids": [9],
        "categories": ["DevOps", "Reliability"],
        "description": "Testing system resilience by injecting failures controlledly.",
        "start_time": "16:00",
        "end_time": "16:45"
    },
    {
        "id": 9,
        "type": "talk",
        "title": "Closing Remarks & Networking",
        "speaker_ids": [8],
        "categories": ["Community", "Networking"],
        "description": "Wrap up of the day and final networking session.",
        "start_time": "17:00",
        "end_time": "17:30"
    }
]

def get_schedule_with_speakers():
    enriched_schedule = []
    for item in SCHEDULE:
        item_copy = item.copy()
        item_speakers = []
        for sp_id in item.get('speaker_ids', []):
            if sp_id in SPEAKERS:
                item_speakers.append(SPEAKERS[sp_id])
        item_copy['speakers_data'] = item_speakers
        enriched_schedule.append(item_copy)
    return enriched_schedule
