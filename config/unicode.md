---
layout: home
---

<div class="container">
  <div class="row">
<%
cp_lookup = Hash[@glyphs.map{|key, value| [value[:codepoint], key]}]
%>
<table>
  <tr>
    <th>&nbsp;</th>
<% for col in 0..15 %>    <th>0x<%= col.to_s(16) %></th>
<% end %>  </tr>
<% for row in (0xe900..0xe9ff).step(16) %>  <tr>
    <th>0x<%= row.to_s(16) %></th>
<% for col in 0..15 %>    <td class="cp<%= row + col %>">
<%
name = cp_lookup[row + col]
unless name.nil? %>      <span class="ai ai-<%= name %> ai-2x" title="<%= name %>"></span>
<% end %>    </td>
<% end %>  </tr>
<% end %>
</table>

</body>
</html>
