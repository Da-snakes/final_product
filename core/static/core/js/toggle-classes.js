

const RemoveClasses = (NewClassNames) => {
  const MatchClasses = NewClassNames.map((Class) => document.body.classList.contains(Class))
  return MatchClasses.indexOf(true) !== -1
}

const ToggleClasses = (Toggle, ClassNames) => {
  const Level = ClassNames.indexOf(Toggle)
  const NewClassNames = ClassNames.slice(0, Level + 1)

  if (RemoveClasses(NewClassNames)) {
    NewClassNames.map((Class) => document.body.classList.remove(Class))
  } else {
    document.body.classList.add(Toggle)
  }
}

export default ToggleClasses
