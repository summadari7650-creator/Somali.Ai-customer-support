import sqlite3
from google import genai

API_KEY = "YOUR_GEMINI_API_KEY"
client = genai.Client(api_key=API_KEY)

def process_issues():
    conn = sqlite3.connect('Somali.AI')
    cursor = conn.cursor()

    query = """
    SELECT ci.issue_id, c.name, ci.problem 
    FROM customer_issues ci
    JOIN customers c ON c."customer-id" = ci.customer_id;
    """
    cursor.execute(query)
    issues = cursor.fetchall()

    print(f"Found {len(issues)} issues to process...\n")

    for issue in issues:
        issue_id, name, problem = issue
        print(f"Processing issue for: {name}...")

        prompt = f"""
        You are an AI customer support assistant for 'Somali AI'.
        Customer Name: {name}
        Customer Complaint: {problem}
        
        Write a professional, empathetic, and polite response in Somali resolving or acknowledging their issue.
        Keep it clear and ready for customer support.
        """

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )
        ai_text = response.text.strip()

        cursor.execute(
            "INSERT INTO ai_responses (issue_id, ai_response) VALUES (?, ?)",
            (issue_id, ai_text)
        )
        conn.commit()
        print(f"Saved response for {name}!")

    conn.close()
    print("\n[Done] Process completed successfully!")

if __name__ == "__main__":
    process_issues()