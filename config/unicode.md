---
layout: home
---

<div class="container">
  <div class="row">

<table>
  <tr>
    <th>&nbsp;</th>
<% for col in 0..15 %>    <th>0x<%= col.to_s(16) %></th>
<% end %>  </tr>
<% for row in (0xe900..0xe9ff).step(16) %>  <tr>
    <th>0x<%= row.to_s(16) %></th>
<% for col in 0..15 %>    <td class="cp<%= row + col %>">
<% name, value = @glyphs.detect { |name, value| value[:codepoint] == row + col }
if value %>      <span class="ai ai-<%= name %> ai-2x" title="<%= name %>"></span>
<% end %>    </td>
<% end %>  </tr>
<% end %>
</table>

</body>
</html>
