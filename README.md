# Course library

Interactive lessons, visual notes and exam practice, organized by course.

- [Start previous-exam practice](https://roseglyph.github.io/course-obb/)
- [Open the course library](https://roseglyph.github.io/course-obb/library.html)
- [Open OOP Lab](https://roseglyph.github.io/course-obb/courses/oop/)
- [Read the compact notes](https://roseglyph.github.io/course-obb/courses/oop/notes/compact.html) or [get the PDF](https://roseglyph.github.io/course-obb/courses/oop/notes/compact.pdf)

## Object-Oriented Programming

OOP Lab contains 22 interactive C++ lessons and 232 explained practice MCQs: 71 reviewed previous-exam questions and 161 lecture-based questions. Change values, trace memory and predict the result. The notes include a 20-page compact edition, a 12-page revision summary and a 53-page detailed reference. Each book is available as standalone HTML, A4 PDF and plain text. The library also links downloadable book packs and an offline copy of the complete lab.

Previous exams is the default practice bank. It consolidates repeated copies from a shared OOP and C exam/question archive; the private authoring records retain the original wording and editing decisions. Answers were reviewed against C++17 and code examples were checked with a compiler. These are study answers, rather than an official answer key or a prediction of the next exam. Lecture-based practice remains available separately, including the instructor exam-focus cue. Browse answers provides a searchable revision library and a TXT download of either bank. Twenty-three questions include diagrams for inheritance, constructor order, copying, member construction and virtual dispatch. Feedback focuses on the answer and reasoning; editorial notes stay in the private authoring records.

Progress stays in the browser, independently for each visitor, with bank-specific statistics. Existing lecture-question progress is preserved. Use the lab's progress export/import controls to move it between devices or between local and hosted copies.

Choose **Calm** or **Persona** in the header. The choice is remembered on this device across the library, lab and HTML notes. Both appearances share the same navigation and learning controls. Switching appearance keeps the current answer and lesson state. Animations respect system reduced-motion preferences.

The root URL currently redirects directly to previous-exam practice. The course chooser remains at `library.html`. To restore it as the root landing page, remove `defaultEntry` from `catalog.json` and run the builder.

The lab opens with immediate-feedback practice: choose an answer, read the explanation, then continue. Mock exam (delayed feedback), retrying misses and the answer library are secondary choices beneath Start. Topics & more filters contains the topics available in the chosen bank and search; instructor exam focus is available in the lecture-based bank.

Lessons put code beside the live memory column on desktop and directly above it on phones. Play, Step and Reset stay within reach; the source window automatically scrolls to the highlighted line. The address-space column separates stack frames, heap targets, static data and instructions, with routes from pointer cells to their targets. Diagrams use symbolic addresses and illustrate a common implementation rather than a mandated physical layout. Questions are shown inside the lesson, give feedback on selection and preserve the experiment.

The **Notes** tab offers compact notes, revision, detailed reference and downloads in short rows. Returning to MCQs from Notes resumes an unfinished session in the same tab. Drag the navigation panel's edge to resize it, or use its width control; click outside or press Escape to close it. The HTML notes retain an ellipsis contents drawer and A4 printing.

## Repository layout

```text
index.html                 Course library, generated from the catalog
catalog.json               Courses, resources and optional tracks
courses/
  oop/
    index.html             Self-contained interactive lab
    notes/                 Compact, summary and reference books
    downloads/             Portable book packs
site/hub.template.html     Course-library layout and behavior
scripts/build_index.py     Catalog builder, Python standard library only
```

## Add a course or track

1. Create a folder under courses with a short stable name. Put its entry page in index.html and its books/downloads beside it.
2. Add a course to catalog.json, including its relative links. Use the OOP entry as the schema example. The builder checks that all referenced resources exist.
3. To group courses into tracks, add entries such as {"id":"foundations","title":"Foundations"} to tracks, then add the IDs to the relevant course's trackIds. The track selector appears when tracks are present. A course can belong to multiple tracks.
4. Run python scripts/build_index.py and commit the generated index.html along with the course files and catalog changes.

The public index contains the rendered catalog, so search and track filtering need no server or runtime data request. The standalone lab and HTML books embed their required styles, code and diagrams. Notes downloaded individually remain readable without the course library.

## GitHub Pages

Publish from the main branch and repository root. The .nojekyll file lets Pages serve the static files directly. All course/resource links use relative paths and support this repository's Pages subpath. Push updates to main to republish.
