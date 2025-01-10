<?php
/* Smarty version 3.1.48, created on 2024-12-05 19:27:53
  from '/var/www/html/admin898sigruz/themes/default/template/controllers/attributes_groups/helpers/list/list_header.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_6751f0a9400f12_70868343',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '4b70b06a28274a991eed71e04fd431057ae1d3fe' => 
    array (
      0 => '/var/www/html/admin898sigruz/themes/default/template/controllers/attributes_groups/helpers/list/list_header.tpl',
      1 => 1733299348,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6751f0a9400f12_70868343 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, true);
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_252857326751f0a93ffa65_21338877', 'leadin');
?>

<?php $_smarty_tpl->inheritance->endChild($_smarty_tpl, "helpers/list/list_header.tpl");
}
/* {block 'leadin'} */
class Block_252857326751f0a93ffa65_21338877 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'leadin' => 
  array (
    0 => 'Block_252857326751f0a93ffa65_21338877',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

	<?php echo '<script'; ?>
 type="text/javascript">
		$(document).ready(function() {
			$(location.hash).click();
		});
	<?php echo '</script'; ?>
>
<?php
}
}
/* {/block 'leadin'} */
}
