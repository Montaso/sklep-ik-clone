<?php
/* Smarty version 3.1.48, created on 2024-11-27 19:27:07
  from '/var/www/html/admin/themes/default/template/controllers/attributes_groups/helpers/list/list_header.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_6747647bc2bd96_89466986',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '6003f61c461219e90e0372e8e10b98804ce30252' => 
    array (
      0 => '/var/www/html/admin/themes/default/template/controllers/attributes_groups/helpers/list/list_header.tpl',
      1 => 1702485415,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6747647bc2bd96_89466986 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, true);
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_663345676747647bc2b4e8_97243105', 'leadin');
?>

<?php $_smarty_tpl->inheritance->endChild($_smarty_tpl, "helpers/list/list_header.tpl");
}
/* {block 'leadin'} */
class Block_663345676747647bc2b4e8_97243105 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'leadin' => 
  array (
    0 => 'Block_663345676747647bc2b4e8_97243105',
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
