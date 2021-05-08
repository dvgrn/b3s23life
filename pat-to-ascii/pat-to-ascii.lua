-- pat-to-ascii.lua
-- select a pattern in Golly, run this script,
--   and a plaintext ASCII format version of
--   the pattern will be copied to the clipboard
--
-- For a variant producing Life Lexicon format, see also
--   http://conwaylife.com/forums/viewtopic.php?p=64427#p64427

local g = golly()
r = g.getselrect()
s=""
for y = 0, r[4] do
  for x = 0, r[3] do
    if g.getcell(x+r[1], y + r[2]) == 1 then
      s = s.."*"
    else
      s = s.."."
    end
  end
  s = s.."\n"
end

g.setclipstr(s)
