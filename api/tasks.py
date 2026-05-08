from celery import shared_task

@shared_task
def notify_new_post(title):
    print(f"New post created: {title}")
    return f"Task completed for {title}"

@shared_task
def check_old_posts():
    print("Checking old posts every minute...")
    return "Periodic task done"