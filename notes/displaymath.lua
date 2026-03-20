-- Pandoc Lua filter: convert DisplayMath to equation* environment
-- This avoids the unicode-math conflict with \[...\] delimiters
function Math(el)
  if el.mathtype == pandoc.DisplayMath then
    return pandoc.RawInline('latex',
      '\\begin{equation*}' .. el.text .. '\\end{equation*}')
  end
end
