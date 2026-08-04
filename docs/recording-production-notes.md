# Recording Production Notes

## API Client: Add POST Support

Status: watch this lesson after publishing/student feedback.

Concern:
- This video had several moving parts while adding POST support to the API client.
- There were failed tests during the recording.
- Some default values/parameters had to be adjusted live.
- The lesson may feel confusing if students are not clear on what changed and why.

Decision for now:
- Keep moving unless feedback/reviews show confusion.
- Do not re-record immediately just because the lesson was messy.

Potential re-record trigger:
- Multiple students complain that the API client POST lesson is hard to follow.
- Reviews mention the framework/client section feels confusing.
- Students cannot reproduce the code after this lesson.

If re-recording this lesson:
1. Start from the checkpoint immediately before this lesson.
2. If a specific pre-POST API client tag exists, use that tag.
3. If not, use:

```bash
git checkout framework-06-auth-helper
```

Then recreate the GET-only API client state first, or checkout the student/public repo commit right before the POST-support video.

Suggested future tag to make this easier:

```text
framework-07-api-client-get
```

Then the re-record flow would be:

```bash
git checkout framework-07-api-client-get
git checkout -b rerecord/api-client-post
```

Clean re-record outline:
1. Show `helpers/auth_helper.py` still calls `requests.post()` directly.
2. Explain: client already handles GET, now it should handle POST too.
3. Add `post()` to `clients/api_client.py`.
4. Add/adjust default `expected_status_code=200`.
5. Add `post_json()` only if it keeps the lesson simple.
6. Refactor `login_user()` to use API client POST.
7. Run the focused login test first.
8. Run protected application tests second.
9. End with: GET and POST now go through the client; next we clean up status-code validation/auth behavior.

Reminder:
- Student repo is source of truth after recording.
- Sync direction after recording is always student → dev.
