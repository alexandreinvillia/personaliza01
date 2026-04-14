## 📚 How to Add a New Assignment

Follow these steps to add a new assignment to the portal:

### 1. Create the Assignment Folder

Create a new folder inside `assignments/` using a short, descriptive, kebab-case name (e.g., `assignments/loops-and-conditionals`).

### 2. Write the README.md

Copy `templates/assignment-template.md` into your new folder as `README.md` and fill in all sections:

> ⚠️ **Important:** Keep section headers **exactly** as they appear in the template, including emoji icons. Do **not** translate or modify the headings.

| Section | Description |
|---|---|
| `# 📘 Assignment: [Title]` | Short, descriptive assignment title |
| `## 🎯 Objective` | 1–2 sentences summarizing learning goals |
| `## 📊 Level` | One of: **Beginner**, **Intermediate**, or **Advanced** |
| `## ✅ Prerequisites` | Concepts/skills required before starting |
| `## 📝 Tasks` | Individual tasks with descriptions and requirements |
| `## 📦 Delivery Criteria` | Checklist of what will be evaluated |
| `## 💡 Tips` | Hints and links to help students |

### 3. Add Starter Files (Optional)

Place any starter code or data files in the same folder (e.g., `starter-code.py`, `data.csv`).

### 4. Register the Assignment in `config.json`

Add an entry to the `assignments` array in `config.json`:

```json
{
  "id": "your-assignment-id",
  "title": "Your Assignment Title",
  "description": "Short description shown in the assignment list.",
  "path": "assignments/your-assignment-id",
  "level": "Beginner",
  "tags": ["python", "loops"],
  "dueDate": "YYYY-MM-DD",
  "attachments": [
    {
      "name": "Starter Code",
      "file": "starter-code.py",
      "type": "python"
    }
  ]
}
```

> **Fields:** `id`, `title`, `description`, and `path` are required. `level`, `tags`, `dueDate`, and `attachments` are optional but recommended.

### 5. Verify

Open `index.html` in a browser (via a local server) to confirm the new assignment appears in the list and the detail page loads correctly.

---

<div align="center">

# 🎉 Congratulations alexandreinvillia! 🎉

<img src="https://octodex.github.com/images/welcometocat.png" height="200px" />

### 🌟 You've successfully completed the exercise! 🌟

## 🚀 Share Your Success!

**Show off your new skills and inspire others!**

<a href="https://twitter.com/intent/tweet?text=I%20just%20completed%20the%20%22Personalize%20Sua%20Experi%C3%AAncia%20com%20o%20GitHub%20Copilot%22%20GitHub%20Skills%20hands-on%20exercise!%20%F0%9F%8E%89%0A%0Ahttps%3A%2F%2Fgithub.com%2Falexandreinvillia%2Fpersonaliza01%0A%0A%23GitHubSkills%20%23OpenSource%20%23GitHubLearn" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Share%20on%20X-1da1f2?style=for-the-badge&logo=x&logoColor=white" alt="Share on X" />
</a>
<a href="https://bsky.app/intent/compose?text=I%20just%20completed%20the%20%22Personalize%20Sua%20Experi%C3%AAncia%20com%20o%20GitHub%20Copilot%22%20GitHub%20Skills%20hands-on%20exercise!%20%F0%9F%8E%89%0A%0Ahttps%3A%2F%2Fgithub.com%2Falexandreinvillia%2Fpersonaliza01%0A%0A%23GitHubSkills%20%23OpenSource%20%23GitHubLearn" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Share%20on%20Bluesky-0085ff?style=for-the-badge&logo=bluesky&logoColor=white" alt="Share on Bluesky" />
</a>
<a href="https://www.linkedin.com/feed/?shareActive=true&text=I%20just%20completed%20the%20%22Personalize%20Sua%20Experi%C3%AAncia%20com%20o%20GitHub%20Copilot%22%20GitHub%20Skills%20hands-on%20exercise!%20%F0%9F%8E%89%0A%0Ahttps%3A%2F%2Fgithub.com%2Falexandreinvillia%2Fpersonaliza01%0A%0A%23GitHubSkills%20%23OpenSource%20%23GitHubLearn" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Share%20on%20LinkedIn-0077b5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Share on LinkedIn" />
</a>

### 🎯 What's Next?

**Keep the momentum going!**

[![](https://img.shields.io/badge/Return%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/alexandreinvillia/personaliza01/issues/1)
[![GitHub Skills](https://img.shields.io/badge/Explore%20GitHub%20Skills-000000?style=for-the-badge&logo=github&logoColor=white)](https://learn.github.com/skills)

*There's no better way to learn than building things!* 🚀

</div>

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

