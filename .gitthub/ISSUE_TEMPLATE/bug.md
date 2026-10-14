name: Bug report
description: Report a defect in the checker, tests, documents or skills
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: "Before opening, please run the checker and tests and include the output."
  - type: textarea
    attributes:
      label: What is wrong
      description: A clear description of the defect.
    validations:
      required: true
  - type: textarea
    attributes:
      label: Reproduct
      description: Steps, the exact command, or the file and lines involved.
    validations:
      required: true
  - type: textarea
    attributes:
      label: Evidence
      description: Checker or test output, or a minimal reporduction.
    validations:
      required: false
