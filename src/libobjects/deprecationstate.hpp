#pragma once

#include "version.hpp"

#include <optional>
#include <string>
#include <vector>

class DeprecationState {
public:
  const std::optional<Version> sinceWhen;
  const std::vector<std::string> replacements;
  const bool deprecated;

  DeprecationState() : deprecated(false) {}

  DeprecationState(const std::string &sinceWhen,
                   const std::vector<std::string> &replacements)
      : sinceWhen(sinceWhen), replacements(replacements), deprecated(true) {}
};
