package connectors

deny[msg] {
  not re_match("^[a-z0-9]+(_[a-z0-9]+)*$", input.entity.name)
  msg := sprintf("Invalid Connector name '%s'. Must be lowercase with underscores", [input.entity.name])
}

deny[msg] {
  not re_match("^[a-z0-9]+(_[a-z0-9]+)*$", input.entity.identifier)
  msg := sprintf("Invalid Connector identifier '%s'. Must be lowercase with underscores", [input.entity.identifier])
}
