# Course library

Interactive lessons, visual notes and exam practice, organized by course.

- [Open the course library](https://roseglyph.github.io/course-obb/)
- [Open OOP Lab](https://roseglyph.github.io/course-obb/courses/oop/)
- [Read the compact notes](https://roseglyph.github.io/course-obb/courses/oop/notes/compact.html) or [get the PDF](https://roseglyph.github.io/course-obb/courses/oop/notes/compact.pdf)

## Object-Oriented Programming

OOP Lab contains 17 interactive C++ lessons and 121 explained practice MCQs. Change values, trace memory and predict the result. The notes include a 16-page compact edition, a 9-page revision summary and a 43-page detailed reference. Each book is available as standalone HTML, A4 PDF and plain text. The library also links downloadable book packs and an offline copy of the complete lab.

The practice bank is for revision; it is not an actual exam paper. Progress stays in the browser. Use the lab's progress export/import controls to move it between devices or between local and hosted copies.

Choose **Calm** or **Persona** in the header. The choice is remembered on this device across the library, lab and HTML notes. Both appearances share the improved navigation and learning controls. Switching appearance keeps the current answer and lesson state. Motion can be switched separately, and system reduced-motion preferences are respected.

The lab opens with immediate-feedback practice: choose an answer, check it, read the explanation, then continue. Mock exam (delayed feedback) reveals explanations at the end. Recall uses a focused deck with self-assessment. The HTML notes use a wider screen layout with an ellipsis contents drawer; printing retains the A4 edition.

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
